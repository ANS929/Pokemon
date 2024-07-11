from .models import MathComment, TCGComment
from django import forms

class MathCommentForm(forms.ModelForm):
    class Meta:
        model = MathComment
        fields = ['name', 'content']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class TCGCommentForm(forms.ModelForm):
    class Meta:
        model = TCGComment
        fields = ['name', 'content']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }