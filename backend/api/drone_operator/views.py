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
        user = get_object_or_404(CustomUser, email=request.data["ownerID"])
        all_drones = DroneInfo.objects.filter(ownerID = user)
        serializer = RegisterDroneSerializer(all_drones, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response(e, status=400)

@api_view(['GET'])
def get_delivering_drones(request):
    '''
    {'cone_count': <number of cones>}
    '''
    LARGE_CAP = 8
    MEDIUM_CAP = 4
    SMALL_CAP = 1
    serializer = RegisterDroneSerializer(data=request.data)
    if serializer.is_valid():
        drone_list = []
        cone_count = request.data["cone_count"]
        objects = DroneInfo.objects.filter(status = "idle")
        large = list(objects.filter(size = 'large'))
        med = list(objects.filter(size = 'medium'))
        small = list(objects.filter(size = 'small'))
        cone_count = drones_by_max(cone_count, large, med, small, drone_list)
        cone_count = drones_by_min(cone_count, large, med, small, drone_list)
        if cone_count > 0:
            return Response("{error: Not enough drones.}")
        return Response(serializer(drone_list, many=True))


def drones_by_max(cone_count, large, med, small, drone_list):
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
            drone_list.append(med.pop())
        else: #This line is where cone_count is less than a larger size but there are no more smaller drones.
            return cone_count
    return cone_count # We reach here if the cones all get drones.

def drones_by_min(cone_count, large, med, small, drone_list):
    LARGE_CAP = 8
    MEDIUM_CAP = 4
    SMALL_CAP = 1
    while cone_count >= 0:
        if cone_count <= MEDIUM_CAP:
            if len(med) > 0:
                drone_list.append(med.pop())
                cone_count -= MEDIUM_CAP
            elif len(large) > 0:
                drone_list.append(large.pop())
                cone_count -= LARGE_CAP
        elif cone_count <= LARGE_CAP:
            if len(large) > 0:
                drone_list.append(large.pop())
                cone_count -= LARGE_CAP
        else:
            return cone_count # Reached if all drones are exhausted
    return cone_count

