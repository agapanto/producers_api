"""producers_api views."""
from rest_framework.viewsets import ModelViewSet
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


class ProducerViewSet(ModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer


class ProductTypeViewSet(ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductPresentationViewSet(ModelViewSet):
    queryset = ProductPresentation.objects.all()
    serializer_class = ProductPresentationSerializer
