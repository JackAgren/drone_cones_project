from rest_framework import serializers
from .models import DroneInfo


class DroneInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DroneInfo
        fields = ['id', 'ownerID', 'status', 'size']
