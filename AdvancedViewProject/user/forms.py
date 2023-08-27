from django import forms
from django.contrib.auth.models import User
from user.models import Profile

class Userform(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "email", "password")
