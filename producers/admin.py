"""Producers_api admin registration."""
from django.contrib import admin
from .models import (
    ProducerType,
    ProducerStatus,
    Producer,
)

admin.site.register(ProducerType)
admin.site.register(ProducerStatus)
admin.site.register(Producer)
