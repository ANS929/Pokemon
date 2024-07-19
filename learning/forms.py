from django import forms
from .models import Student
from account.models import Profile
from django.contrib.auth.models import User
from learning.models import Course, EnrolledStudent

# create a new class
class NewCourseForm(forms.ModelForm):
    title = forms.CharField(max_length=30)
    description = forms.CharField(max_length=200)

    class Meta:
        model = Course
        fields = ('title', 'description')

# assign a student to a teacher's roster
class AddStudentForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=User.objects.filter(profile__is_student=True),
        label="Select Student",
        widget=forms.Select(attrs={'class': 'form-control'}),
        to_field_name='id',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].label_from_instance = self.label_from_user_instance

    def label_from_user_instance(self, obj):
        return f"{obj.first_name} {obj.last_name}"

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
            self.fields['student'].queryset = Student.objects.filter(
                user__profile__is_student=True)

    class Meta:
        model = Student
        fields = ['student']

# enroll a student in a class
class EnrollStudentForm(forms.ModelForm):
    student = forms.ModelChoiceField(
        queryset=None,
        label="Select Student",
        widget=forms.Select(attrs={'class': 'form-control'}),
        to_field_name='id',
    )

    def __init__(self, *args, teacher=None, course=None, **kwargs):
        super().__init__(*args, **kwargs)
        if teacher and course:
            self.fields['student'].queryset = User.objects.filter(
                profile__is_student=True
            ).exclude(
                enrollments__course=course
            ).distinct()
        self.fields['student'].label_from_instance = self.label_from_instance

    def label_from_instance(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    class Meta:
        model = EnrolledStudent
        fields = ['student']

# unenroll a student from a class
class UnenrollStudentForm(forms.ModelForm):
    student = forms.ModelChoiceField(
        queryset=None,
        label="Select Student to Unenroll",
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    def __init__(self, *args, course=None, **kwargs):
        super().__init__(*args, **kwargs)
        if course:
            self.fields['student'].queryset = EnrolledStudent.objects.filter(course=course).select_related('student')

        self.fields['student'].label_from_instance = self.label_from_instance

    def label_from_instance(self, obj):
        return f"{obj.student.first_name} {obj.student.last_name}"

    class Meta:
        model = EnrolledStudent
        fields = ['student']