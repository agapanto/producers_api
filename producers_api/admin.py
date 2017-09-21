"""Producers_api admin registration."""
from django.contrib import admin
from .models import (
    ProducerType,
    ProducerStatus,
    Producer,
    ProductType,
    Product,
    ProductPresentation,
)

admin.site.register(ProducerType)
admin.site.register(ProducerStatus)
admin.site.register(Producer)
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(ProductPresentation)
