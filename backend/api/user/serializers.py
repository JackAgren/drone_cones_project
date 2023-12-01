from rest_framework import serializers
from .models import CustomUser

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password', 'is_staff', 'is_superuser']


class UsersSerializerEmail(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email']