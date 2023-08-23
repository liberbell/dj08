from django.shortcuts import render, redirect
from .models import Items

# Create your views here.

def item_list(request):
    items = Items.objects.all()
    return render(request, 'store/item_list.html',
                  context={'items': items})

def item_detal(request, id):
    item = Items.objects.filter(pk=id).first()
    return render(request, "store/item_detail.html",
                  context={'item': item})

def to_google(request):
    return redirect("https://google.com")
