from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Practice, CompletedPractice, Quiz, CompletedQuiz, Student, EnrolledStudent, Course
from .forms import NewCourseForm, AddStudentForm, AssignStudentForm

def index(request):
    return render(request, 'learning/base.html')

def learning_home(request):
    return render(request, 'learning/learning.html')

def parents(request):
    return render(request, 'learning/parents.html')

def students(request):
    return render(request, 'learning/students.html')

def teachers(request):
    return render(request, 'learning/teachers.html')

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

#practice slug
def practice_detail(request, practice_slug):
    practice = get_object_or_404(Practice, slug=practice_slug)
    context = {
        'practice': practice,
    }
    return render(request, f'learning/{practice_slug}.html', context)

# parent dashboard
def parent_dashboard(request):
    return render(request, 'learning/parent_dashboard.html')

# student dashboard
@login_required
def student_dashboard(request):
    if not request.user.profile.is_student:
        return HttpResponse("You do not have permission to view this page.")

    completed_practices = CompletedPractice.objects.filter(student=request.user)
    completed_quizzes = CompletedQuiz.objects.filter(student=request.user)

    context = {
        'completed_practices': completed_practices,
        'completed_quizzes': completed_quizzes,
    }

    return render(request, 'learning/student_dashboard.html', context)

# teacher dashboard
@login_required
def teacher_dashboard(request):
    if not request.user.profile.is_teacher:
        return HttpResponse("You do not have permission to view this page.")

    courses = Course.objects.filter(teacher=request.user)
    enrolled_students = EnrolledStudent.objects.filter(course__teacher=request.user)
    all_students = Student.objects.all()

    context = {
        'courses': courses,
        'enrolled_students': enrolled_students,
        'all_students': all_students,
    }
    return render(request, 'learning/teacher_dashboard.html', context)

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

        return redirect('learning:student_dashboard')

    context = {
        'quiz': quiz,
    }
    return render(request, f'learning/{quiz_slug}.html', context)

# practice submission
@login_required
def submit_practice(request, practice_slug):
    practice = get_object_or_404(Practice, slug=practice_slug)
    user = request.user

    if request.method == 'POST':
        CompletedPractice.objects.create(student=user, practice=practice)
        return redirect('learning:student_dashboard')

    return render(request, 'learning/comparing_whole.html', {'practice': practice})

# create a new class
@login_required
def NewCourse(request):
    if request.method == 'POST':
        form = NewCourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.teacher = request.user
            course.save()
            return redirect('learning:teacher_dashboard')
    else:
        form = NewCourseForm()

    context = {
        'form':form
    }

    return render(request, 'learning/new_course.html', context)

# edit a class
@login_required
def EditCourse(request):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = NewCourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('learning:teacher_dashboard')
    else:
        form = NewCourseForm(instance=course)

    context = {
        'form': form,
        'course': course
    }

    return render(request, 'learning/edit_course.html', context)

# assign a student to a teacher
@login_required
def AddStudent(request):
    if not request.user.profile.is_teacher:
        return HttpResponse("You do not have permission to view this page.")

    if request.method == 'POST':
        form = AddStudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.name = form.cleaned_data['name']
            student.save()
            return redirect('learning:teacher_dashboard')
    else:
        form = AddStudentForm()
    
    context = {
        'form': form
    }
    return render(request, 'learning/add_student.html', context)

# assign a student to a course
@login_required
def AssignStudent(request, course_id):
    if not request.user.profile.is_teacher:
        return HttpResponse("You do not have permission to view this page.")

    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = AssignStudentForm(request.POST)
        if form.is_valid():
            student = form.cleaned_data['student']
            EnrolledStudent.objects.create(student=student, course=course)
            return redirect('learning:teacher_dashboard')
    else:
        form = AssignStudentForm()

    context = {
        'form': form,
        'course': course
    }
    return render(request, 'learning/assign_student.html', context)