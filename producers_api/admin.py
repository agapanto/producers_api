"""Producers_api admin registration."""
from django.contrib import admin
from .models import (
    Producer,
    ProductType,
    Product,
    ProductPresentation,
)

admin.site.register(Producer)
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(ProductPresentation)
