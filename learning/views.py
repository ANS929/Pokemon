from django.shortcuts import render

def index(request):
    return render(request, 'learning/base.html')

def learning_home(request):
    return render(request, 'learning/learning.html')