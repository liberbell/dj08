from django import forms
from .models import Users
from django.contrib.auth.password_validation import validate_password


class RegistForm(forms.ModelForm):
    username = forms.CharField(label="Name:")
    age = forms.IntegerField(label="Age:", min_value=0)
    email = forms.EmailField(label="Email:")
    password = forms.CharField(label="Password:", widget=forms.PasswordInput())
    confirm_password = forms.CharField(label="Confirm Password:", widget=forms.PasswordInput())

    class Meta():
        model = Users
        fields = ("username", "age", "email", "password")

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data["password"]
        confirm_password = cleaned_data["confirm_password"]
        if password != confirm_password:
            raise forms.ValidationError("Invalid password")
        
    def save(self, commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data['password'], user)
        user.set_password(self.cleaned_data["password"])
        user.save()
        return user
    
class LoginForm(forms.Form):
    email = forms.CharField(label="Email:")
    password = forms.CharField(label="Password:", widget=forms.PasswordInput())

class UserEditForm(forms.ModelForm):
    username = forms.CharField(label="Username:")
    age = forms.IntegerField(label="Age:", min_value=0)
    email = forms.EmailField(label="Emil:")
    picture = forms.FileField(label="Picture:", required=False)

    class Meta():
        model = Users
        fields = ("username", "age", "email", "picture")