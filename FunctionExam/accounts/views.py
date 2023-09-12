from django.shortcuts import render, redirect
from . import forms
from django.core.exceptions import ValidationError
from .models import UserActivateTokens
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, "accounts/home.html")

def regist(request):
    regist_form = forms.RegistForm(request.POST or None)
    if regist_form.is_valid():
        try:
            regist_form.save()
            return redirect("accounts:home")
        except ValidationError as e:
            regist_form.add_error("password", e)

    return render(request, 'accounts/regist.html',
                  context={
                      "regist_form": regist_form,
                  })

def activate_user(request, token):
    user_activate_tokne = UserActivateTokens.objects.activate_user_by_token(token)
    return render(request, "accounts/activate_user.html")

def user_login(request):
    login_form = forms.LoginForm(request.POST or None)
    if login_form.is_valid():
        email = login_form.cleaned_data.get("email")
        password = login_form.cleaned_data.get("password")
        user = authenticate(email=email, password=password)
        if user.is_active:
            login(request, user)
            return redirect("accounts:home")
        else:
            pass
    pass

def user_logout(request):
    pass