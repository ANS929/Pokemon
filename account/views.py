from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import Profile

def index(request):
    return render(request, 'learning/base.html')

def account(request):
    return render(request, 'account/account.html')

def login_page(request):
    return render(request, 'account/login.html')

def register_page(request):
    return render(request, 'account/register.html')

def settings(request):
    return render(request, 'account/settings.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            role = form.cleaned_data.get('role')
            if role == 'student' or role == 'teacher':
                # Create profile only if role is student or teacher
                profile = Profile(user=user)
                if role == 'student':
                    profile.is_student = True
                elif role == 'teacher':
                    profile.is_teacher = True
                profile.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}. You can now log in.")
            return redirect('account:login')
    else:
        form = UserRegistrationForm()

    return render(request, 'account/register.html', {'user_form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                auth_login(request, user)
                if user.is_superuser:
                    return redirect('admin:index')  # Redirect admin to Django admin panel
                else:
                    return redirect('learning:index')  # Redirect others to main app index
            else:
                return HttpResponse("Your account is disabled.")
        else:
            messages.error(request, "Invalid login details supplied.")
            return redirect('account:login')
    else:
        return render(request, 'account/login.html')

@login_required    
def user_logout(request):
    auth_logout(request)
    return redirect(reverse('learning:index'))

@login_required    
def student_dashboard(request):
    try:
        if request.user.profile.is_student:
            return render(request, 'learning/student_dashboard.html')
        else:
            return HttpResponse("You do not have permission to view this page.")
    except Profile.DoesNotExist:
        return HttpResponse("You do not have permission to view this page.")

@login_required
def teacher_dashboard(request):
    try:
        if request.user.profile.is_teacher:
            return render(request, 'learning/teacher_dashboard.html')
        else:
            return HttpResponse("You do not have permission to view this page.")
    except Profile.DoesNotExist:
        return HttpResponse("You do not have permission to view this page.")