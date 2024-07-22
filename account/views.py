from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, ProfileUpdateForm, UserUpdateForm
from .models import Profile
from registration.backends.simple.views import RegistrationView
from django.urls import reverse_lazy
from django.contrib import messages

# website homepage
def index(request):
    return render(request, 'learning/base.html')

# account page
def account(request):
    return render(request, 'account/account.html')

# login
def login_page(request):
    return render(request, 'registration/login.html')

# registration complete
def registration_complete(request):
    return render(request, 'registration/registration_complete.html')

# custom registration (inclusion of teacher/stuent/parent role)
class custom_registration_view(RegistrationView):
    form_class = UserRegistrationForm

    def register(self, form_class):
        new_user = form_class.save(commit=False)
        new_user.set_password(form_class.cleaned_data['password'])
        new_user.save()

        profile, created = Profile.objects.get_or_create(user=new_user)
        role = form_class.cleaned_data.get('role')

        if role == 'student':
            profile.is_student = True
            profile.is_teacher = False
            profile.is_parent = False
        elif role == 'teacher':
            profile.is_teacher = True
            profile.is_student = False
            profile.is_parent = False
        elif role == 'parent':
            profile.is_teacher = False
            profile.is_student = False
            profile.is_parent = True

        profile.save()

        return new_user

    def get_success_url(self, user=None):
        return reverse_lazy('account:registration_complete')

# user profile
@login_required
def profile(request):
    return render(request, 'account/profile.html')

# update user profile
@login_required
def profile_update(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile Updated Successfully!')
            return redirect('account:profile')
    else:
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'account/profile_update.html', context)