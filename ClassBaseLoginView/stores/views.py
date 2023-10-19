from typing import Any
from django.db.models.query import QuerySet
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

    def get_queryset(self):
        query = super().get_queryset()
        product_type_name = self.request.GET.get("product_type_name", None)
        if product_type_name:
            query = query.filter(product_type__name=product_type_name)
        return query
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_type_name"] = self.request.GET.get("product_type_name", "None")
        context["product_name"] = self.request.GET.get("product_name", "None")
        return context