from django.shortcuts import render
from user.forms import Userform, ProfileForm


# Create your views here.
def user_list(request):
    return render(request, "user/user_list.html")

def index(request):
    return render(request, "user/index.html")

def register(request):
    user_form = Userform(request.POST or None)