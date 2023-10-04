from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"

class RegistUserView(CreateView):
    template_name = "regist.html"
    form_class = RegistForm