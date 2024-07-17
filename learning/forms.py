from django import forms
from .models import Course, Student, EnrolledStudent
from account.models import Profile
from django.contrib.auth.models import User

# create a new class
class NewCourseForm(forms.ModelForm):
    title = forms.CharField(max_length=30)
    description = forms.CharField(max_length=200)

    class Meta:
        model = Course
        fields = ('title', 'description')

# assign a student to a teacher
class AddStudentForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.filter(profile__is_student=True), label="Select User")

    class Meta:
        model = Student
        fields = ['user', 'name']

# assign a student to a class
class AssignStudentForm(forms.ModelForm):
    student = forms.ModelChoiceField(queryset=User.objects.filter(profile__is_student=True), label="Select Student")

    class Meta:
        model = EnrolledStudent
        fields = ['student']