from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import (
    Products,
)
import os


# Create your views here.
class ProductListView(LoginRequiredMixin, ListView):
    model = Products
    template_name = os.path.join("stores", "product_list.html")