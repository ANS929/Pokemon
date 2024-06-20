from django.shortcuts import render

def index(request):
    return render(request, 'education/base.html')

def education_home(request):
    return render(request, 'education/education.html')

