from rest_framework.decorators import api_view, authentication_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import DroneInfoSerializer, RegisterDroneSerializer
from .models import DroneInfo
from user.models import CustomUser
from datetime import datetime
from django.shortcuts import get_object_or_404


@api_view(['POST'])
def register_drone(request):
    serializer = RegisterDroneSerializer(data=request.data)
    if serializer.is_valid():
        user = get_object_or_404(CustomUser, email=request.data["ownerID"])
        DroneInfo.objects.create(
                ownerID=user,
                size=request.data['size'],
                status=request.data['status']
                )
        return Response(serializer.data, 201)
    return Response(serializer.errors, 400)


@api_view(['POST'])
def update_status(request):
    return Response({'Response': 'UPDATE_CONFIRMATION'})


@api_view(['GET'])
def get_status(request):
    return Response({'Response': 'DRONE_STATUS'})


@api_view(['POST'])
def decomission_drone(request):
    return Response({'Response': 'DECOMISSION_CONFIRMATION'})


@api_view(['GET'])
def get_all_owned_drones(request):
    return Response({'Response': 'ALL_OWNED_DRONES'})
