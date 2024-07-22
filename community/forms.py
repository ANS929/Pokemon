from .models import MathComment, TCGComment
from django import forms

# comment on math forum
class MathCommentForm(forms.ModelForm):
    class Meta:
        model = MathComment
        fields = ['content']

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

# comment on tcg forum
class TCGCommentForm(forms.ModelForm):
    class Meta:
        model = TCGComment
        fields = ['content']

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }