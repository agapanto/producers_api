"""producers_api views."""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import (
    ProducerType,
    ProducerStatus,
    Producer,
)
from .serializers import (
    ProducerTypeSerializer,
    ProducerStatusSerializer,
    ProducerSerializer,
)


class ProducerTypeViewSet(ModelViewSet):
    queryset = ProducerType.objects.all()
    serializer_class = ProducerTypeSerializer


class ProducerStatusViewSet(ModelViewSet):
    queryset = ProducerStatus.objects.all()
    serializer_class = ProducerStatusSerializer


class ProducerViewSet(ModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
