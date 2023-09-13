from django.shortcuts import render

# Create your views here.
def create_theme(request):
    create_theme_form = forms.CreateThemesForm(request.POST or None)