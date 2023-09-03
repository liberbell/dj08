from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import UserChangeForm, UserCreationForm

# Register your models here.
User = get_user_model()

class CustomizeUserAdmin(UserAdmin):
    form = UserChangeForm