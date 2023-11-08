from rest_framework import serializers
from .models import Orders, Cones


class ConesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cones
        fields = ['id', 'cone', 'toppings', 'cost',]


class OrdersSerializer(serializers.ModelSerializer):
    cones = ConesSerializer(many=True)
    class Meta:
        model = Orders
        fields = ['id', 'userID', 'droneID', 'cones', 'location', 'timeOrdered', 'timeDelivered']