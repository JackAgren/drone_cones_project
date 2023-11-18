from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import DroneInfoSerializer, RegisterDroneSerializer
from .models import DroneInfo
from user.models import CustomUser
from datetime import datetime
from django.shortcuts import get_object_or_404
from rest_framework import generics

@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
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
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
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
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def decomission_drone(request):
    serializer = RegisterDroneSerializer(data=request.data)
    if serializer.is_valid():
        object = DroneInfo.objects.get(id = request.data["droneID"])
        object.delete()
        return Response({'success': f'Drone {request.droneID}\'s has been decommissioned.'})
    return Response(serializer.errors, status=400)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_all_owned_drones(request):
    '''
    {
    'ownerID': <Owner Email>
    }
    '''
    try:
        if 'email' in request.query_params:
            user = CustomUser.objects.get(email=request.query_params['email'])
            all_drones = DroneInfo.objects.filter(ownerID = user)
        else:
            all_drones = DroneInfo.objects.all()
        return Response(RegisterDroneSerializer(all_drones, many=True).data)
    except Exception as e:
        print(e)
        return Response({"detail": "Not found."}, status=400)
