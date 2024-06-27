from django.shortcuts import render

def index(request):
    return render(request, 'learning/base.html')

def account_home(request):
    return render(request, 'account/account.html')

def login(request):
    return render(request, 'account/login.html')

def register(request):
    return render(request, 'account/register.html')

def settings(request):
    return render(request, 'account/settings.html')