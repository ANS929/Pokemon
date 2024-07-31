from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Practice, CompletedPractice, Quiz, CompletedQuiz, Student, EnrolledStudent, Course, RegisteredStudent, User, RegisteredChild, Student, Badge, CompletedBadge, Unit, GradeLevel, CompletedUnit
from .forms import AddStudentForm, RemoveStudentForm, EnrollStudentForm, NewCourseForm, AddChildForm, RemoveChildForm
from community.models import MathQuestion, TCGQuestion
from django.contrib import messages

# website homepage
def index(request):
    recent_math_questions = MathQuestion.objects.order_by('-date_created')[:2]
    recent_tcg_questions = TCGQuestion.objects.order_by('-date_created')[:2]
    
    context = {
        'recent_math_questions': recent_math_questions,
        'recent_tcg_questions': recent_tcg_questions,
    }
    return render(request, 'learning/base.html', context)

# learning homepage
def learning_home(request):
    return render(request, 'learning/learning.html')

# parent page
def parents(request):
    return render(request, 'learning/parents.html')

# student page
def students(request):
    return render(request, 'learning/students.html')

# teacher page
def teachers(request):
    return render(request, 'learning/teachers.html')

# grade-level pages
def gr1(request):
    return render(request, 'learning/gr1.html')

def gr2(request):
    return render(request, 'learning/gr2.html')

def gr3(request):
    return render(request, 'learning/gr3.html')

def gr4(request):
    return render(request, 'learning/gr4.html')

def gr5(request):
    return render(request, 'learning/gr5.html')

def gr6(request):
    return render(request, 'learning/gr6.html')

def gr7(request):
    return render(request, 'learning/gr7.html')

def gr8(request):
    return render(request, 'learning/gr8.html')

# quiz slug
@login_required
def quiz_detail(request, quiz_slug):
    quiz = get_object_or_404(Quiz, slug=quiz_slug)
    context = {
        'quiz': quiz,
    }
    return render(request, f'learning/{quiz_slug}.html', context)

# practice slug
@login_required
def practice_detail(request, practice_slug):
    practice = get_object_or_404(Practice, slug=practice_slug)
    context = {
        'practice': practice,
    }
    return render(request, f'learning/{practice_slug}.html', context)

# unit slug
@login_required
def unit_detail(request, unit_slug):
    unit = get_object_or_404(Unit, slug=unit_slug)
    context = {
        'unit': unit,
    }
    return render(request, f'learning/{unit_slug}.html', context)

# student dashboard
@login_required
def student_dashboard(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    if (request.user == user or
        (request.user.profile.is_parent and RegisteredChild.objects.filter(parent=request.user, student=user).exists()) or
        (request.user.profile.is_teacher and RegisteredStudent.objects.filter(teacher=request.user, student=user).exists())):
        
        completed_practices = CompletedPractice.objects.filter(student=user).order_by('-date_completed')
        completed_quizzes = CompletedQuiz.objects.filter(student=user).order_by('-date_completed')
        badges = Badge.objects.all()
        completed_badges = CompletedBadge.objects.filter(student=user).select_related('badge')

        badges_with_status = []
        for badge in badges:
            completed_badge = completed_badges.filter(badge=badge).first()
            badges_with_status.append({
                'badge': badge,
                'completed': completed_badge is not None,
                'date_completed': completed_badge.date_completed if completed_badge else None
            })

        context = {
            'student': user,
            'completed_practices': completed_practices,
            'completed_quizzes': completed_quizzes,
            'badges_with_status': badges_with_status,
        }

        return render(request, 'learning/student_dashboard.html', context)
    else:
        return HttpResponse("You do not have permission to view this page.")

# practice submission
@login_required
def submit_practice(request, practice_slug):
    practice = get_object_or_404(Practice, slug=practice_slug)
    user = request.user

    if CompletedPractice.objects.filter(student=user, practice=practice).exists():
        messages.error(request, f"You have already submitted the practice '{practice.title}'.")
        return redirect('learning:student_dashboard', user_id=user.id)

    if request.method == 'POST':
        if user.profile.is_student:
            CompletedPractice.objects.create(student=user, practice=practice)
            
            # check for Alpha Badge (completion of first practice)
            if not CompletedBadge.objects.filter(student=user, badge__name='Alpha Badge').exists():
                if CompletedPractice.objects.filter(student=user).count() == 1:
                    badge = Badge.objects.get(name='Alpha Badge')
                    CompletedBadge.objects.create(student=user, badge=badge)
                    messages.success(request, "Congratulations! You've earned the Alpha Badge!")

            check_unit_completion(request, user)

            return redirect('learning:student_dashboard', user_id=user.id)
        else:
            return HttpResponse("Only students can submit practices.")

    return render(request, '', {'practice': practice})

# quiz submission
@login_required
def submit_quiz(request, quiz_slug):
    quiz = get_object_or_404(Quiz, slug=quiz_slug)
    user = request.user
    score = 0

    if request.method == 'POST':
        if user.profile.is_student:
            correct_answers = quiz.correct_answers

            # check if the student has already achieved a perfect score for the quiz
            if CompletedQuiz.objects.filter(student=user, quiz=quiz, score=5).exists():
                messages.error(request, "You have already achieved a perfect score for this quiz.")
                return redirect('learning:student_dashboard', user_id=user.id)

            for question, correct_answer in correct_answers.items():
                user_answer = request.POST.get(question).strip()
                if user_answer.lower() == correct_answer.lower():
                    score += 1

            perfect_score = (score == 5)
            completed_quiz = CompletedQuiz.objects.create(student=user, quiz=quiz, score=score, perfect_score=perfect_score)

            # check for Beta Badge (completion of first quiz)
            if not CompletedBadge.objects.filter(student=user, badge__name='Beta Badge').exists():
                if CompletedQuiz.objects.filter(student=user).count() == 1:
                    badge = Badge.objects.get(name='Beta Badge')
                    CompletedBadge.objects.create(student=user, badge=badge)
                    messages.success(request, "Congratulations! You've earned the Beta Badge!")

            # check for Delta Badge (improvement of a previous quiz score)
            if not CompletedBadge.objects.filter(student=user, badge__name='Delta Badge').exists():
                improvement = completed_quiz.get_improvement()
                if improvement > 0:
                    badge = Badge.objects.get(name='Delta Badge')
                    CompletedBadge.objects.create(student=user, badge=badge)
                    messages.success(request, "Congratulations! You've earned the Delta Badge!")

            check_unit_completion(request, user)

            return redirect('learning:student_dashboard', user_id=user.id)
        else:
            return HttpResponse("Only students can submit quizzes.")

    context = {
        'quiz': quiz,
    }
    return render(request, f'learning/{quiz_slug}.html', context)

# parent dashboard
@login_required
def parent_dashboard(request):
    user = request.user
    if not user.profile.is_parent:
        return HttpResponse("You do not have permission to view this page.")

    all_children = User.objects.filter(profile__is_student=True)
    registered_children = RegisteredChild.objects.filter(parent=user)

    context = {
        'all_children': all_children,
        'registered_children': registered_children,
    }
    return render(request, 'learning/parent_dashboard.html', context)

# add a child to a parent's roster
@login_required
def add_child(request):
    if not request.user.profile.is_parent:
        return HttpResponse("You do not have permission to view this page.")
    
    if request.method == 'POST':
        form = AddChildForm(request.POST, parent=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Child added successfully.')
            return redirect('learning:parent_dashboard')
    else:
        form = AddChildForm(parent=request.user)

    context = {
        'form': form
    }
    return render(request, 'learning/add_child.html', context)

# remove a child from a parent's roster
@login_required
def remove_child(request):
    if not request.user.profile.is_parent:
        return HttpResponse("You do not have permission to view this page.")

    if request.method == 'POST':
        form = RemoveChildForm(request.POST, parent=request.user)
        if form.is_valid():
            registered_child = form.cleaned_data['student']
            if registered_child:
                registered_child.delete()
                messages.success(request, 'Child removed successfully.')
                return redirect('learning:parent_dashboard')
    else:
        form = RemoveChildForm(parent=request.user)

    context = {
        'form': form
    }
    return render(request, 'learning/remove_child.html', context)

# teacher dashboard
@login_required
def teacher_dashboard(request):
    user = request.user
    if not request.user.profile.is_teacher:
        return HttpResponse("You do not have permission to view this page.")

    courses = Course.objects.filter(teacher=user)
    enrolled_students = EnrolledStudent.objects.filter(course__teacher=user)
    all_students = Student.objects.all()
    registered_students = RegisteredStudent.objects.filter(teacher=user)

    context = {
        'courses': courses,
        'enrolled_students': enrolled_students,
        'all_students': all_students,
        'registered_students': registered_students,
    }
    return render(request, 'learning/teacher_dashboard.html', context)

# create a new class
@login_required
def new_course(request):
    if request.method == 'POST':
        form = NewCourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.teacher = request.user
            course.save()
            return redirect('learning:view_class', course_id=course.id)
    else:
        form = NewCourseForm()

    context = {
        'form': form
    }

    return render(request, 'learning/new_course.html', context)

# view a class
@login_required
def view_course(request, course_id):
    user = request.user
    course = get_object_or_404(Course, id=course_id)
    enrolled_students = EnrolledStudent.objects.filter(course=course)

    if not user.profile.is_teacher:
        return HttpResponse("You do not have permission to view this page.")

    context = {
        'course': course,
        'enrolled_students': enrolled_students
    }
    return render(request, 'learning/view_course.html', context)

# edit a class
@login_required
def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = NewCourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, f'Course updated successfully!')
            return redirect('learning:view_class', course_id=course.id)
    else:
        form = NewCourseForm(instance=course)

    context = {
        'form': form,
        'course': course
    }

    return render(request, 'learning/edit_course.html', context)

# delete a class
@login_required
def delete_course(request, course_id):
    user = request.user
    course = get_object_or_404(Course, id=course_id)

    if not user.profile.is_teacher:
        return HttpResponse("You do not have permission to view this page.")

    if request.method == 'POST':
        course.delete()
        messages.success(request, f"The class '{course.title}' has been deleted.")
        return redirect('learning:teacher_dashboard')

    return render(request, 'learning/delete_course.html', {'course': course})

# add a student to a teacher's roster
@login_required
def add_student(request):
    if not request.user.profile.is_teacher:
        return HttpResponse("You do not have permission to view this page.")

    if request.method == 'POST':
        form = AddStudentForm(request.POST, teacher=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully.')
            return redirect('learning:teacher_dashboard')
    else:
        form = AddStudentForm(teacher=request.user)

    context = {
        'form': form
    }
    return render(request, 'learning/add_student.html', context)

# remove a student from a teacher's roster
@login_required
def remove_student(request):
    if not request.user.profile.is_teacher:
        return HttpResponse("You do not have permission to view this page.")

    if request.method == 'POST':
        form = RemoveStudentForm(request.POST, user=request.user)
        if form.is_valid():
            registered_student = form.cleaned_data['student']
            if registered_student:
                registered_student.delete()
                messages.success(request, 'Student removed successfully.')
                return redirect('learning:teacher_dashboard')
    else:
        form = RemoveStudentForm(user=request.user)

    context = {
        'form': form
    }
    return render(request, 'learning/remove_student.html', context)

# enroll a student in a class
@login_required
def enroll_student(request, course_id):
    if not request.user.profile.is_teacher:
        return HttpResponse("You do not have permission to view this page.")

    course = get_object_or_404(Course, id=course_id)
    form = EnrollStudentForm(request.POST or None, teacher=request.user, course=course)

    if request.method == 'POST' and form.is_valid():
        student = form.cleaned_data['student']
        if not EnrolledStudent.objects.filter(student=student, course=course).exists():
            EnrolledStudent.objects.create(student=student, course=course)
            messages.success(request, f"{student.get_full_name()} has been enrolled in {course.title}.")
            return redirect('learning:view_class', course_id=course.id)
        else:
            form.add_error('student', 'This student is already enrolled in the course.')

    context = {
        'form': form,
        'course': course,
    }
    return render(request, 'learning/enroll_student.html', context)

# unenroll a student from a class
@login_required
def unenroll_student(request, course_id, student_id):
    if not request.user.profile.is_teacher:
        return HttpResponse("You do not have permission to view this page.")

    course = get_object_or_404(Course, id=course_id)
    enrolled_student = get_object_or_404(
        EnrolledStudent, student_id=student_id, course=course
    )

    if request.method == 'POST':
        enrolled_student.delete()
        messages.success(request, f"{enrolled_student.student.get_full_name()} has been unenrolled from {course.title}.")
        return redirect('learning:view_class', course_id=course.id)

    context = {
        'enrolled_student': enrolled_student,
        'course': course,
    }
    return render(request, 'learning/unenroll_student.html', context)

# check whether a unit has been completed
def check_unit_completion(request, user):
    if not user.profile.is_student:
        return
    
    units = Unit.objects.all()
    for unit in units:
        print(f"Unit: {unit.name}, Grade Level: {unit.grade_level.name}")
    
    for unit in units:
        completed_practices = all(
            CompletedPractice.objects.filter(student=user, practice=practice).exists()
            for practice in unit.practices.all()
        )
        completed_quiz = CompletedQuiz.objects.filter(student=user, quiz=unit.quiz).exists()
        
        print(f"Unit: {unit.name}, Completed Practices: {completed_practices}, Completed Quiz: {completed_quiz}")

        if completed_practices and completed_quiz:
            if not CompletedUnit.objects.filter(student=user, unit=unit).exists():
                CompletedUnit.objects.create(student=user, unit=unit)
                print(f"Unit Completed: {unit.name} for user {user.username}")

            # check for Pi Badge (completion of a unit)
            if not CompletedBadge.objects.filter(student=user, badge__name='Pi Badge').exists():
                badge = Badge.objects.get(name='Pi Badge')
                CompletedBadge.objects.create(student=user, badge=badge)
                messages.success(request, "Congratulations! You've earned the Pi Badge!")
                print(f"Pi Badge Awarded to {user.username}")

    grade_levels = GradeLevel.objects.all()
    print(f"Available Grade Levels: {[grade_level.name for grade_level in grade_levels]}")

    for grade_level in grade_levels:
        units_in_grade_level = Unit.objects.filter(grade_level=grade_level)
        print(f"Grade Level: {grade_level.name}, Units in Grade Level: {[unit.name for unit in units_in_grade_level]}")

        if not units_in_grade_level.exists():
            print(f"No units found for grade level: {grade_level.name}")
            continue

        completed_units_count = CompletedUnit.objects.filter(student=user, unit__in=units_in_grade_level).count()
        print(f"Grade Level: {grade_level.name}, Total Units: {units_in_grade_level.count()}, Completed Units: {completed_units_count}")

        all_units_completed = completed_units_count == units_in_grade_level.count()

        if all_units_completed:
            all_units_quiz_completed = all(
                CompletedQuiz.objects.filter(student=user, quiz=unit.quiz).exists()
                for unit in units_in_grade_level
            )
            
            print(f"All Quizzes Completed for Grade Level {grade_level.name}: {all_units_quiz_completed}")

            if all_units_quiz_completed:
                # check for Infinity Badge (completion of a grade level)
                if not CompletedBadge.objects.filter(student=user, badge__name='Infinity Badge').exists():
                    badge = Badge.objects.get(name='Infinity Badge')
                    CompletedBadge.objects.create(student=user, badge=badge)
                    messages.success(request, "Congratulations! You've earned the Infinity Badge!")
                    print(f"Infinity Badge Awarded to {user.username}")

# quiz answer explanations
@login_required
def quiz_explanations(request, quiz_slug):
    quiz = get_object_or_404(Quiz, slug=quiz_slug)
    user = request.user

    completed_quizzes = CompletedQuiz.objects.filter(student=user, quiz=quiz, score=5).order_by('-date_completed')

    if not completed_quizzes.exists():
        messages.error(request, "You must score 5/5 on this quiz to view the explanations.")
        return redirect('learning:student_dashboard', user_id=user.id)

    completed_quiz = completed_quizzes.first()

    context = {
        'quiz': quiz,
        'correct_answers': quiz.correct_answers,
        'completed_quiz': completed_quiz
    }
    return render(request, f'learning/explanations_{quiz_slug}.html', context)