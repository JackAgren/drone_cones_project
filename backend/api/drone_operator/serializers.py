from rest_framework import serializers
from .models import DroneInfo


class DroneInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DroneInfo
        fields = ['ownerID', 'status', 'size']

class RegisterDroneSerializer(serializers.Serializer):
    ownerID = serializers.CharField()
    size = serializers.CharField()
    status = serializers.CharField()
