from django import forms
from .models import Letters


class LettersForm(forms.ModelForm):
    class Meta:
        model = Letters
        fields = ['letter']
