"""producers_api views."""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import (
    ProducerType,
    ProducerStatus,
    Producer,
    ProductType,
    Product,
    ProductPresentation,
)
from .serializers import (
    ProducerTypeSerializer,
    ProducerStatusSerializer,
    ProducerSerializer,
    ProductTypeSerializer,
    ProductSerializer,
    ProductPresentationSerializer,
    ProductsByProducerSerializer,
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
                valid_rows.append(serializer.validated_data)
            else:
                invalid_rows.append(serializer.validated_data)

        for row in valid_rows:
            product_type, created = ProductType.objects.get_or_create(name=row.get('product_type_name'))
            producer, created = Producer.objects.get_or_create(name=row.get('producer_name'))
            product, created = Product.objects.get_or_create(name=row.get('product_name'), producer=producer)
            product, created = ProductPresentation.objects.get_or_create(name=row.get('product_presentation_name'), product=product, price=row.get('product_presentation_price'), description=row.get('product_presentation_description'))

        return Response(
            {
                "valid": valid_rows,
                "invalid": invalid_rows
            }
        )
