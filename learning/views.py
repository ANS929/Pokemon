from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Practice, CompletedPractice, Quiz, CompletedQuiz, Student, EnrolledStudent, Course, RegisteredStudent, User, Child, RegisteredChild, Student, Badge, CompletedBadge
from .forms import AddStudentForm, RemoveStudentForm, EnrollStudentForm, NewCourseForm, AddChildForm, RemoveChildForm
from django.contrib import messages

# website homepage
def index(request):
    return render(request, 'learning/base.html')

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
def quiz_detail(request, quiz_slug):
    quiz = get_object_or_404(Quiz, slug=quiz_slug)
    context = {
        'quiz': quiz,
    }
    return render(request, f'learning/{quiz_slug}.html', context)

# practice slug
def practice_detail(request, practice_slug):
    practice = get_object_or_404(Practice, slug=practice_slug)
    context = {
        'practice': practice,
    }
    return render(request, f'learning/{practice_slug}.html', context)

# student dashboard
@login_required
def student_dashboard(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    if (request.user == user or
        (request.user.profile.is_parent and RegisteredChild.objects.filter(parent=request.user, student=user).exists()) or
        (request.user.profile.is_teacher and RegisteredStudent.objects.filter(teacher=request.user, student=user).exists())):
        
        completed_practices = CompletedPractice.objects.filter(student=user)
        completed_quizzes = CompletedQuiz.objects.filter(student=user)
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
        CompletedPractice.objects.create(student=user, practice=practice)
        
        if not CompletedBadge.objects.filter(student=user, badge__name='Alpha Badge').exists():
            if CompletedPractice.objects.filter(student=user).count() == 1:
                badge = Badge.objects.get(name='Alpha Badge')
                CompletedBadge.objects.create(student=user, badge=badge)
                messages.success(request, "Congratulations! You've earned the Alpha Badge!")

        return redirect('learning:student_dashboard', user_id=user.id)

    return render(request, '', {'practice': practice})

# quiz submission
@login_required
def submit_quiz(request, quiz_slug):
    quiz = get_object_or_404(Quiz, slug=quiz_slug)
    user = request.user
    score = 0

    if request.method == 'POST':
        correct_answers = quiz.correct_answers

        for question, correct_answer in correct_answers.items():
            user_answer = request.POST.get(question).strip()
            if user_answer.lower() == correct_answer.lower():
                score += 1

        CompletedQuiz.objects.create(student=user, quiz=quiz, score=score)

        return redirect('learning:student_dashboard', user_id=user.id)

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