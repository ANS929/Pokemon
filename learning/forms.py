from django import forms
from .models import Student
from account.models import Profile
from django.contrib.auth.models import User

# # create a new class
# class NewCourseForm(forms.ModelForm):
#     title = forms.CharField(max_length=30)
#     description = forms.CharField(max_length=200)

#     class Meta:
#         model = Course
#         fields = ('title', 'description')



# assign a student to a teacher's roster
class AddStudentForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=User.objects.filter(profile__is_student=True),
        label="Select Student",
        widget=forms.Select(attrs={'class': 'form-control'}),
        to_field_name='id',
    )

    class Meta:
        model = Student
        fields = ['user']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.name = f"{instance.user.first_name} {instance.user.last_name}"
        if commit:
            instance.save()
        return instance

# remove a student from a teacher's roster
class RemoveStudentForm(forms.ModelForm):
    student = forms.ModelChoiceField(
        queryset=Student.objects.none(),
        label="Select Student to Remove",
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(RemoveStudentForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['student'].queryset = Student.objects.filter(user__profile__is_student=True)

    class Meta:
        model = Student
        fields = ['student']