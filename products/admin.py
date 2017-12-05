"""Producers_api admin registration."""
from django.contrib import admin
from .models import (
    ProductType,
    Product,
    ProductPresentation,
)

admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(ProductPresentation)
