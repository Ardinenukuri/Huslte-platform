from rest_framework import serializers
from .models import CustomUser, Bike, Customer, Sale

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'name', 'is_active', 'is_staff']

class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = ['id', 'name', 'description', 'price', 'quantity', 'image']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone_number']

class SaleSerializer(serializers.ModelSerializer):
    bike = BikeSerializer()
    customer = CustomerSerializer()

    class Meta:
        model = Sale
        fields = ['id', 'bike', 'customer', 'quantity', 'date']
