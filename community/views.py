from django.shortcuts import render

def index(request):
    return render(request, 'learning/base.html')

def community_home(request):
    return render(request, 'community/community.html')

def math_forum(request):
    return render(request, 'community/math_forum.html')

def tcg_forum(request):
    return render(request, 'community/tcg_forum.html')
