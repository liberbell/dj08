from django.shortcuts import render
from . import forms

# Create your views here.
def home(request):
    return render(request, "accounts/home.html")

def regist(request):
    regist_fomr = forms.RegistForm(request.POST)