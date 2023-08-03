from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    return render(request, "formapp/index.html")

def form_page(request):
    form = forms.UserInfo()
    if request.method == "POST":
        form = forms.UserInfo(request.POST)
    return render(request, "formapp/form_page.html", context={
        "form": form
    })