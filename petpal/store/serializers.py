from rest_framework import serializers
from .models import Store, Product, GroomingService

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['store_id', 'store_name', 'location', 'store_type', 'store_owner']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'product_name', 'price', 'stock_status', 'store']

class GroomingServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroomingService
        fields = ['service_id', 'service_name', 'pet_type', 'price', 'duration', 'store']
