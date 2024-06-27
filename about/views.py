from django.shortcuts import render

def index(request):
    return render(request, 'learning/base.html')

def about_home(request):
    return render(request, 'about/about.html')

def site(request):
    return render(request, 'about/site.html')

def tcg(request):
    return render(request, 'about/tcg.html')