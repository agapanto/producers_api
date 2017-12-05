"""producers_api models."""
from django.conf import settings
from django.db import models


class Store(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
