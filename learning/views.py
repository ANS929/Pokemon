from django.shortcuts import render

def index(request):
    return render(request, 'learning/base.html')

def learning_home(request):
    return render(request, 'learning/learning.html')

def parents(request):
    return render(request, 'learning/parents.html')

def students_home(request):
    return render(request, 'learning/students_home.html')

def teachers(request):
    return render(request, 'learning/teachers.html')

def classes(request):
    return render(request, 'learning/classes.html')

def students(request):
    return render(request, 'learning/students.html')

def children(request):
    return render(request, 'learning/children.html')

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

def dashboard(request):
    return render(request, 'learning/dashboard.html')

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

def classifying_shapes(request):
    return render(request, 'learning/classifying_shapes.html')

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