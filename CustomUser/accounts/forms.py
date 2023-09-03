from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import User

user = get_user_model()

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label="Password:", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Reinpu password:", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email", "password")
