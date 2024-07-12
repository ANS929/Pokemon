from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher')
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            profile, created = Profile.objects.get_or_create(user=user)
            role = self.cleaned_data.get('role')
            if role == 'student':
                profile.is_student = True
                profile.is_teacher = False
            elif role == 'teacher':
                profile.is_teacher = True
                profile.is_student = False
            profile.save()
        return user