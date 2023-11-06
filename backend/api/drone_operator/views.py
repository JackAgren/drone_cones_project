from rest_framework.decorators import api_view, authentication_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import DroneInfoSerializer
from .models import DroneInfo
from datetime import datetime


@api_view(['POST'])
def register_drone(request):
    try:
        DroneInfo.objects.create(
                ownerID=request.data["ownerID"],
                size=request.data["size"],
                status="commissoned"
                )
    except KeyError:
        return Response({'error': 'BAD REQUEST'})
    except Exception as err:
        return Response({'error': str(err)})
    return Response({'success': "DRONE REGISTERED"})


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
