"""producers_api urls."""
from rest_framework import serializers
from .models import (
    Producer,
    ProductType,
    Product,
    ProductPresentation,
)


class ProducerSerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Producer
        fields = '__all__'

    def get_products_count(self, obj):
        return obj.product_set.count()


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
    product_presentation_price = serializers.FloatField()
    # producer_name = serializers.CharField()
    product_presentation_description = serializers.CharField(required=False, allow_blank=True, allow_null=True)
