from rest_framework import serializers
from .models import OrderModel
from .models import OrderItemModel
from apps.clients.serializers import ClientModelSerializer, AddressModelSerializer
from apps.products.serializers import ProductModelSerializer

class OrderItemModelSerializer(serializers.ModelSerializer):
    product = ProductModelSerializer()
    class Meta:
        model = OrderItemModel
        fields = '__all__'

        
class OrderModelSerializer(serializers.ModelSerializer):
    client = ClientModelSerializer()
    address = AddressModelSerializer()
    orderitemmodel_set = OrderItemModelSerializer(many=True)

    class Meta:
        model = OrderModel
        fields = '__all__'
