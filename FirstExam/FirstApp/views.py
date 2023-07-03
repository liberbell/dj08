from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def add(request, num1, num2):
    return HttpResponse(f"<h1>")