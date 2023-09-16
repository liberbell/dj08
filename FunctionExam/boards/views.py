from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from .models import Themes

# Create your views here.
def create_theme(request):
    create_theme_form = forms.CreateThemeForm(request.POST or None)

    if create_theme_form.is_valid():
        create_theme_form.instance.user = request.user
        create_theme_form.save()
        messages.success(request, "Theme created successfully")
        return redirect("accounts:home")
    
    return render(request, "boards/create_theme.html",
                  context={
                      "create_theme_form": create_theme_form
                  })
def list_themes(request):
    themes = Themes.objects.fetch_all_theme()
    return render(request, "boards/list_themes.html",
                  context={
                      "themes": themes
                  })
