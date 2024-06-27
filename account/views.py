from django.shortcuts import render

def index(request):
    return render(request, 'learning/base.html')

def account_home(request):
    return render(request, 'account/account.html')