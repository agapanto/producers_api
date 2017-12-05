"""producers_api models."""
from django.conf import settings
from django.db import models


class ProducerType(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)+" - "+str(self.created_at)


class ProducerStatus(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)+" - "+str(self.created_at)


class Producer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=100)
    producer_type = models.ForeignKey(ProducerType, blank=True, null=True)
    status = models.ForeignKey(ProducerStatus)
