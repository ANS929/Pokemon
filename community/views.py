from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import MathQuestion, TCGQuestion

def index(request):
    return render(request, 'learning/base.html')

def community_home(request):
    return render(request, 'community/community.html')

def math_forum(request):
    return render(request, 'community/math_forum.html')

def tcg_forum(request):
    return render(request, 'community/tcg_forum.html')

class MathQuestionListView(ListView):
    model = MathQuestion
    template_name = 'community/math_forum.html'
    context_object_name ='questions'
    ordering = ['-date_created']

class TCGQuestionListView(ListView):
    model = TCGQuestion
    template_name = 'community/tcg_forum.html'
    context_object_name ='questions'
    ordering = ['-date_created']

class MathQuestionDetailView(DetailView):
    model = MathQuestion

class TCGQuestionDetailView(DetailView):
    model = TCGQuestion