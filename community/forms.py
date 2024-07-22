from .models import MathComment, TCGComment
from django import forms

# comment on math forum
class MathCommentForm(forms.ModelForm):
    class Meta:
        model = MathComment
        fields = ['name', 'content']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

# comment on tcg forum
class TCGCommentForm(forms.ModelForm):
    class Meta:
        model = TCGComment
        fields = ['name', 'content']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }