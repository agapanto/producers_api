"""Producers_api models."""
from django.conf import settings
from django.db import models

class Producer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.contact_email)+" - "+str(self.created_at)


class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.contact_email)+" - "+str(self.created_at)
