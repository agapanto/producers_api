"""producers_api views."""
from rest_framework.response import Response
from rest_framework.views import APIView
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


# CSV IMPORT ENDPOINTS
class ProductsByProducerApiView(APIView):
    def get(self, request, format=None):
        """Return a list of all imports."""
        return Response({})

    def post(self, request, format=None):
        """Import a csv file."""
        return Response({})
