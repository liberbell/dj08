from django import forms
from .models import Users


class RegistForm(forms.ModelForm):
    username = forms.CharField(label="Name:")
    age = forms.IntegerField(label="Age:")