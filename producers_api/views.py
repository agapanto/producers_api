"""producers_api views."""
from rest_framework import viewsets
# from rest_framework_apicontrol.permissions import HasApiKeyPermission
from .models import (
    Producer,
    ProductType,
    Product,
    ProductPresentation,
)
from .serializers import (
    ProducerSerializer,
    ProductTypeSerializer,
    ProductSerializer,
    ProductPresentationSerializer,
)


class ProducerViewSet(viewsets.ModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer


class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductPresentationViewSet(viewsets.ModelViewSet):
    queryset = ProductPresentation.objects.all()
    serializer_class = ProductPresentationSerializer
