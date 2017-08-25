"""producers_api views."""
from rest_framework import status
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
    ProductsByProducerSerializer,
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

    def post(self, request, *args, **kwargs):
        """Import a csv file."""

        invalid_rows = []
        valid_rows = []

        for row in request.data.get('data'):
            row_data = {
                'product_type_name': row.get('TIPO'),
                'product_name': row.get('PRODUCTO'),
                'producer_name': row.get('PRODUCTOR'),
                'product_presentation_name': row.get('UNIDAD'),
                'product_presentation_price': row.get('PRECIO'),
                'product_presentation_description': row.get('OBSERVACIONES')
            }

            serializer = ProductsByProducerSerializer(
                data=row_data
            )

            if serializer.is_valid():
                valid_rows.append(row)
            else:
                invalid_rows.append(row)

        return Response({})
