from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Good bye</h1>")

def user_page(request, user_name):
    return HttpResponse(f"<h1>{user_name}\'s page</h1>")

def number_page(request, user_name, number):
    return HttpResponse(f"<h1>{user_name}\'s page number={number}</h1>")