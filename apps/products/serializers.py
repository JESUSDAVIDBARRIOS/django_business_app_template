from rest_framework import serializers
from .models import ProductModel

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        exclude = ['created_at', 'updated_at']