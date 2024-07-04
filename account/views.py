from django.shortcuts import render, redirect
from account.forms import UserForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

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

def register(request):
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        
        if user_form.is_valid():
            user = user_form.save()
            registered = True
            return redirect('registration_success')  # Replace with your success URL or logic
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    
    return render(request, 'account/register.html', {
        'user_form': user_form,
        'registered': registered
    })

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('learning:index'))
            else:
                return HttpResponse("Your Pokemon account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'account/login.html')

@login_required    
def user_logout(request):
    logout(request)
    return redirect(reverse('learning:index;'))