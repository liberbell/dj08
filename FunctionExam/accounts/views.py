from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "accounts/home.html")

def regist(request):
    regist_fomr = forms.RegistForm(request.POST)