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