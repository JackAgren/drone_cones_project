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
        curr_cap = 0
        drone_list = []
        cone_count = request.data["cone_count"]
        objects = DroneInfo.objects.filter(status = "idle")
        large = list(objects.filter(size = 'large'))
        med = list(objects.filter(size = 'medium'))
        small = list(objects.filter(size = 'small'))


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
        else:
            return cone_count
    return cone_count

def drones_by_min(cone_count, large, med, small, drone_list):
