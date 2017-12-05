"""producers_api models."""
from django.conf import settings
from django.db import models
from producers.models import (
    Producer,
)


class ProductType(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)+" - "+str(self.created_at)


class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=100)
    producer = models.ForeignKey(Producer)

    def __str__(self):
        return str(self.name)+" - "+str(self.created_at)


class ProductPresentation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product)
    price = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return str(self.name)+" - "+str(self.created_at)
