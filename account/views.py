from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from .models import Profile
from registration.backends.simple.views import RegistrationView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

def index(request):
    return render(request, 'learning/base.html')

def account(request):
    return render(request, 'account/account.html')

def login_page(request):
    return render(request, 'registration/login.html')

def settings(request):
    return render(request, 'account/settings.html')

def registration_complete(request):
    return render(request, 'registration/registration_complete.html')

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
    
class CustomRegistrationView(RegistrationView):
    form_class = UserRegistrationForm

    def register(self, form_class):
        new_user = form_class.save(commit=False)
        new_user.set_password(form_class.cleaned_data['password'])
        new_user.save()

        if not hasattr(new_user, 'profile'):
            profile = Profile(user=new_user)
            role = form_class.cleaned_data.get('role')
            if role == 'student':
                profile.is_student = True
            elif role == 'teacher':
                profile.is_teacher = True
            profile.save()
        
        return new_user
    
    def get_success_url(self, user=None):
        return reverse_lazy('account:registration_complete') 

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(username=username, password=password)

#         if user:
#             if user.is_active:
#                 auth_login(request, user)
#                 if user.is_superuser:
#                     return redirect('admin:index')  
#                 else:
#                     return redirect('learning:index') 
#             else:
#                 return HttpResponse("Your account is disabled.")
#         else:
#             messages.error(request, "Invalid login details supplied.")
#             return redirect('account:login')
#     else:
#         return render(request, 'registration/login.html')

# @login_required    
# def user_logout(request):
#     auth_logout(request)
#     return redirect(reverse('learning:index'))
   
# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()

#             role = form.cleaned_data.get('role')
#             if role == 'student' or role == 'teacher':
#                 # Check if user already has a profile
#                 profile = user.profile
#                 if role == 'student':
#                     profile.is_student = True
#                 elif role == 'teacher':
#                     profile.is_teacher = True
#                 profile.save()

#             username = form.cleaned_data.get('username')
#             messages.success(request, f"Account created for {username}. You can now log in.")
#             return redirect('account:login')
#     else:
#         form = UserRegistrationForm()

#     return render(request, 'registration/registration_form.html', {'form': form})