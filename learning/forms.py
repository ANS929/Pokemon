from django import forms
from .models import Student
from account.models import Profile
from django.contrib.auth.models import User
from learning.models import Course, EnrolledStudent, RegisteredStudent

# create a new class
class NewCourseForm(forms.ModelForm):
    title = forms.CharField(max_length=30)
    description = forms.CharField(max_length=200)

    class Meta:
        model = Course
        fields = ('title', 'description')

# assign a student to a teacher's roster
class AddStudentForm(forms.ModelForm):
    student = forms.ModelChoiceField(
        queryset=User.objects.none(),
        label="Select Student",
        widget=forms.Select(attrs={'class': 'form-control'}),
        to_field_name='id',
    )

    def __init__(self, *args, **kwargs):
        self.teacher = kwargs.pop('teacher', None)
        super().__init__(*args, **kwargs)
        if self.teacher:
            registered_students_ids = RegisteredStudent.objects.filter(teacher=self.teacher).values_list('student_id', flat=True)
            self.fields['student'].queryset = User.objects.filter(
                profile__is_student=True
            ).exclude(
                id__in=registered_students_ids
            ).distinct()
        self.fields['student'].label_from_instance = self.label_from_user_instance

    def label_from_user_instance(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    class Meta:
        model = RegisteredStudent
        fields = ['student']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.teacher = self.teacher
        if commit:
            instance.save()
        return instance

# remove a student from a teacher's roster
class RemoveStudentForm(forms.Form):
    student = forms.ModelChoiceField(
        queryset=RegisteredStudent.objects.none(),
        label="Select Student to Remove",
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['student'].queryset = RegisteredStudent.objects.filter(teacher=user)
            self.fields['student'].label_from_instance = self.get_student_label

    def get_student_label(self, obj):
        return f"{obj.student.get_full_name()}"

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
            registered_students = RegisteredStudent.objects.filter(
                teacher=teacher
            ).exclude(
                student__enrollments__course=course
            ).values_list('student', flat=True)

            self.fields['student'].queryset = User.objects.filter(
                id__in=registered_students
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