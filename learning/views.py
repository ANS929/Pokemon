from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

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

def ns_quiz(request):
    return render(request, 'learning/ns_quiz.html')

def at_quiz(request):
    return render(request, 'learning/at_quiz.html')

def comp_quiz(request):
    return render(request, 'learning/comp_quiz.html')

def da_quiz(request):
    return render(request, 'learning/da_quiz.html')

def geo_quiz(request):
    return render(request, 'learning/geo_quiz.html')

def meas_quiz(request):
    return render(request, 'learning/meas_quiz.html')

def parent_dashboard(request):
    return render(request, 'learning/parent_dashboard.html')

@login_required
def student_dashboard(request):
    if request.user.profile.is_student:
        return render(request, 'dashboard/student.html')
    else:
        return HttpResponse("You do not have permission to view this page.")

@login_required
def teacher_dashboard(request):
    if request.user.profile.is_teacher:
        return render(request, 'dashboard/teacher.html')
    else:
        return HttpResponse("You do not have permission to view this page.")