from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import UserChangeForm, UserCreationForm

# Register your models here.
User = get_user_model()

class CustomizeUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ("username", "email", "is_staff")
    fieldset = (
        ("User information",
            {"fields": ("username", "email", "password", "website", "picture")}
        ),
        ("Permissions", 
            {"fields": ("is_staff", "is_active", "is_supersuer")}
        ),
    )

    add_fieldsets = (
        ("User information",
            {"fields": ("username", "email", "password", "confirm_password")}),
    )