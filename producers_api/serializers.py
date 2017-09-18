"""producers_api urls."""
from rest_framework import serializers
from .models import (
    Producer,
    ProductType,
    Product,
    ProductPresentation,
)


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = '__all__'


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductPresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPresentation
        fields = '__all__'


# CSV IMPORT SERIALIZERS
class ProductsByProducerSerializer(serializers.Serializer):
    product_type_name = serializers.CharField()
    product_name = serializers.CharField()
    producer_name = serializers.CharField()
    # producer_name = serializers.CharField()
    product_presentation_name = serializers.CharField()
    product_presentation_price = serializers.IntegerField()
    # producer_name = serializers.CharField()
    product_presentation_description = serializers.CharField(required=False, allow_blank=True, allow_null=True)
