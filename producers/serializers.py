"""producers_api urls."""
from rest_framework import serializers
from .models import (
    ProducerType,
    ProducerStatus,
    Producer,
)


class ProducerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProducerType
        fields = '__all__'


class ProducerStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProducerStatus
        fields = '__all__'


class ProducerSerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Producer
        fields = '__all__'

    def get_products_count(self, obj):
        return obj.product_set.count()
