from django.shortcuts import render

def index(request):
    return render(request, 'learning/base.html')

def community_home(request):
    return render(request, 'community/community.html')