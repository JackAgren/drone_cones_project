from rest_framework import serializers
from .models import Inventory, RestockOrders


class InventorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inventory
        fields = ['quantity', 'costPerUnit', 'category', 'dateFilled', 'description', 'salesPrice']

class DescriptionSerializer(serializers.Serializer):
    description = serializers.CharField()

class RestockReportSerializer(serializers.Serializer):
    cost = serializers.FloatField()
    item = serializers.CharField()

