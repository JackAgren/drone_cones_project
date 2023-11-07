from rest_framework import serializers
from .models import Inventory

class InventorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inventory
        fields = ['quantity', 'costPerUnit', 'category', 'dateFilled', 'description', 'salesPrice']
