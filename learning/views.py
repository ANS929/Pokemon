from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Practice, CompletedPractice, Quiz, CompletedQuiz

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

def your_classes(request):
    return render(request, 'learning/your_classes.html')

def your_students(request):
    return render(request, 'learning/your_students.html')

def your_children(request):
    return render(request, 'learning/your_children.html')

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

def comparing_whole(request):
    return render(request, 'learning/comparing_whole.html')

def comparing_decimal(request):
    return render(request, 'learning/comparing_decimal.html')

def add_subtract(request):
    return render(request, 'learning/add_subtract.html')

def multiplication(request):
    return render(request, 'learning/multiplication.html')

def rw_whole(request):
    return render(request, 'learning/rw_whole.html')

def rw_fraction(request):
    return render(request, 'learning/rw_fraction.html')

def symmetry(request):
    return render(request, 'learning/symmetry.html')

def identifying_shapes(request):
    return render(request, 'learning/identifying_shapes.html')

def converting_units(request):
    return render(request, 'learning/converting_units.html')

def area_perimeter(request):
    return render(request, 'learning/area_perimeter.html')

def representing(request):
    return render(request, 'learning/representing.html')

def interpreting(request):
    return render(request, 'learning/interpreting.html')

def quiz_detail(request, quiz_slug):
    quiz = get_object_or_404(Quiz, slug=quiz_slug)
    context = {
        'quiz': quiz,
    }
    return render(request, f'learning/{quiz_slug}.html', context)

def parent_dashboard(request):
    return render(request, 'learning/parent_dashboard.html')

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

@login_required
def teacher_dashboard(request):
    if request.user.profile.is_teacher:
        return render(request, 'learning/teacher_dashboard.html')
    else:
        return HttpResponse("You do not have permission to view this page.")
    
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