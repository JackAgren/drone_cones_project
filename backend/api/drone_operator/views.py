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
    '''
    ./drone_operator/register_drone

    {
    "ownerID": <ID>,
    "size": <size>,
    status: <status>
    }
    '''
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
    '''
        ./drone_operator/update_status
        BODY:
        {
        "droneID": <id>, 
        "status": <new status> 
        }
    '''
    serializer = RegisterDroneSerializer(data=request.data)
    if serializer.is_valid():
        object = DroneInfo.objects.get(id = request.data["droneID"])
        setattr(object, 'status', request.data["status"])
        return Response({'success': f'Drone {request.droneID}\'s status is now {object.status}'})
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_status(request):
    serializer = RegisterDroneSerializer(data=request.data)
    if serializer.is_valid():
        object = DroneInfo.objects.get(id = request.data["droneID"])
        return Response({'status': f'{object.status}'})
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def decomission_drone(request):
    serializer = RegisterDroneSerializer(data=request.data)
    if serializer.is_valid():
        object = DroneInfo.objects.get(id = request.data["droneID"])
        object.delete()
        return Response({'success': f'Drone {request.droneID}\'s has been decommissioned.'})
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_all_owned_drones(request):
    '''
    {
    'ownerID': <Owner Email>
    }
    '''
    serializer = RegisterDroneSerializer(data=request.data)
    if serializer.is_valid():
        all_drones = DroneInfo.objects.filter(ownerID = request.data['ownerID'])
        return Response(serializer(all_drones, many=True).data)
    return Response(serializer.errors, status=400)