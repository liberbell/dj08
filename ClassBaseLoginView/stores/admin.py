from django.contrib import admin
from .models import (
    ProductTypes, ProductPictures, Products, Manufacturers
)

# Register your models here.
admin.site.register(
    [ProductTypes, Products, Manufacturers, ProductPictures]
)