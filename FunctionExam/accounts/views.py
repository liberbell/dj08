from django.shortcuts import render
from . import forms

# Create your views here.
def home(request):
    return render(request, "accounts/home.html")

def regist(request):
    regist_form = forms.RegistForm(request.POST)
    if regist_form.is_valid():
        regist_form.save()

    return render(request, 'accounts/regist.html',
                  context={
                      "resit_form": regist_form,
                  })