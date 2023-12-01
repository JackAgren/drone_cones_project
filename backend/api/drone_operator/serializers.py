from rest_framework import serializers
from .models import DroneInfo
from user.serializers import UsersSerializerEmail


class DroneInfoSerializer(serializers.HyperlinkedModelSerializer):
    ownerID = UsersSerializerEmail()

    class Meta:
        model = DroneInfo
        fields = ['id','ownerID', 'status', 'size']

class RegisterDroneSerializer(serializers.Serializer):
    ownerID = serializers.CharField()
    size = serializers.CharField()
    status = serializers.CharField()
