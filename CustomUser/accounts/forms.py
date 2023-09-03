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

    def clena(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise ValidationError("Invalid password")
    
    def save(self):
        user= super().save(commit=False)
        user.set_password(self.cleaned_data.get("password"))
        user.save()
        return user
    
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    website = forms.URLField(required=False)
    picture = forms.FileField(required=False)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            "is_staff",
            "is_active",
            "website",
            "picture"
            )

    def clean_password(self):
        return self.initial["password"]