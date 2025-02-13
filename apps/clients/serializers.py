from rest_framework import serializers
from .models import ClientModel, AddressModel

class AddressModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressModel
        fields = '__all__'

class ClientModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientModel
        fields = '__all__'