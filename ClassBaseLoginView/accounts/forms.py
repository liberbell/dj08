from django import forms
from .models import Users
from django.contrib.auth.password_validation import validate_password

class RegistForm(forms.ModelForm):