from django.shortcuts import render

def index(request):
    return render(request, 'learning/base.html')

def about_home(request):
    return render(request, 'about/about.html')