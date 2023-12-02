import json
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.admin.views.decorators import staff_member_required
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
#@staff_member_required
def register_drone(request):
    '''
    ./drone_operator/register_drone

    {
    "ownerID": <Owner Email>,
    "size": <size>,
    status: <status>
    }
    '''
    serializer = RegisterDroneSerializer(data=request.data)
    if serializer.is_valid():
        user = get_object_or_404(CustomUser, email=request.data["ownerID"])
        drone = DroneInfo.objects.create(
                ownerID=user,
                size=request.data['size'],
                status=request.data['status']
                )
        serialized = DroneInfoSerializer(drone)
        return Response(serialized.data, 201)
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
    try:
        drone = DroneInfo.objects.get(id = request.data["droneID"])
        drone.status = request.data["status"]
        drone.save()
        serialized = DroneInfoSerializer(drone)
        return Response(serialized.data)
    except Exception as e:
        return Response({"error": str(e)}, status=400)


@api_view(['GET'])
def get_status(request):
    '''
    {
    'droneID': <Drone Id>
    }
    '''
    try:
        drone = DroneInfo.objects.get(id = request.query_params["droneID"])
        serialized = DroneInfoSerializer(drone)
        return Response({'status': serialized.data["status"]})
    except Exception as e:
        return Response({"error": str(e)}, status=400)


@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def decomission_drone(request):
    try:
        drone = DroneInfo.objects.get(id = request.data['id'])
        drone.delete()
        return Response({'deleted': request.data['id']})
    except Exception as e:
        return Response({"detail": e}, status=404)



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
        user = get_object_or_404(CustomUser, email=request.query_params["ownerID"])
        all_drones = DroneInfo.objects.filter(ownerID = user)
        serializer = DroneInfoSerializer(all_drones, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)}, status=400)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_delivering_drones(request):
    '''
    {'cone_count': <number of cones>}
    '''
    drone_list = []
    cone_count = int(request.query_params["cone_count"])
    available_drones = DroneInfo.objects.filter(status = "active")
    large = list(available_drones.filter(size = 'large'))
    med = list(available_drones.filter(size = 'medium'))
    small = list(available_drones.filter(size = 'small'))
    cone_count = optimal_assignment(cone_count, large, med, small, drone_list)
    cone_count = fill_assignment(cone_count, large, med, small, drone_list)
    if cone_count > 0:
        return Response({"error": "Not enough drones."})
    all_drones = DroneInfoSerializer(drone_list, many=True)
    return Response(all_drones.data)

def optimal_assignment(cone_count, large, med, small, drone_list):
    LARGE_CAP = 8
    MEDIUM_CAP = 4
    SMALL_CAP = 1
    while cone_count >= 0:
        if cone_count >= LARGE_CAP and len(large) > 0:
            drone_list.append(large.pop())
            cone_count -= LARGE_CAP  
        elif cone_count >= MEDIUM_CAP and len(med) > 0:
            drone_list.append(med.pop())
            cone_count -= MEDIUM_CAP
        elif cone_count >= SMALL_CAP and len(small) > 0:
            cone_count -= SMALL_CAP
            drone_list.append(small.pop())
        else: #This line is where cone_count is less than a larger size but there are no more smaller drones.
            return cone_count
    return cone_count # We reach here if the cones all get drones.

def fill_assignment(cone_count, large, med, small, drone_list):
    LARGE_CAP = 8
    MEDIUM_CAP = 4
    SMALL_CAP = 1
    while cone_count >= 0:
        if len(small) > 0:
            cone_count -= SMALL_CAP
            drone_list.append(small.pop())
        elif len(med) > 0:
            drone_list.append(med.pop())
            cone_count -= MEDIUM_CAP
        elif len(large) > 0:
            drone_list.append(large.pop())
            cone_count -= LARGE_CAP  
        else: #This line is where cone_count is less than a larger size but there are no more smaller drones.
            return cone_count
    return cone_count # We reach here if the cones all get drones.

