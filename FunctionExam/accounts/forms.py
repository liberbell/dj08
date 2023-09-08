from django import forms
from .models import Users


class RegistForm(forms.ModelForm):
    username = forms.CharField(label="Name:")
    age = forms.IntegerField(label="Age:", min_value=0)
    email = forms.EmailField(label="Email:")
    password = forms.CharField(label="Password:", widget=forms.PasswordInput())