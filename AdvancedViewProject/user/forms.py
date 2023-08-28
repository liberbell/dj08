from django import forms
from django.contrib.auth.models import User
from user.models import Profile

class Userform(forms.ModelForm):
    username = forms.CharField(label="Username")
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "email", "password")

class ProfileForm(forms.ModelForm):
    website = forms.URLField(label="Website")
    picture = forms.FileField(label="Picture")

    class Meta:
        model = Profile
        fields = ("website","picture")

class LoginForm(forms.Form):
    usrename = forms.CharField(label="Name:", max_length=150)
    password = forms.CharField(label="Password:", widget=forms.PasswordInput())
