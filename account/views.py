from django.shortcuts import render, redirect
from account.forms import UserForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm

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
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = user.profile  # Access the profile related to this user
            profile.is_student = form.cleaned_data.get('is_student')
            profile.is_teacher = form.cleaned_data.get('is_teacher')
            profile.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You can now log in.')
            return redirect('account-login')  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()
    
    return render(request, 'account/register.html', {'form': form})

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

@login_required
def student_dashboard(request):
    if request.user.profile.is_student:
        # Render student dashboard
        return render(request, 'learning:student_dashboard')
    else:
        # Redirect or show access denied message
        return HttpResponse("You do not have permission to view this page.")

@login_required
def teacher_dashboard(request):
    if request.user.profile.is_teacher:
        # Render teacher dashboard
        return render(request, 'learning:teacher_dashboard')
    else:
        # Redirect or show access denied message
        return HttpResponse("You do not have permission to view this page.")