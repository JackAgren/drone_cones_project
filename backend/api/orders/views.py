from rest_framework.decorators import api_view, authentication_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import ConesSerializer, OrdersSerializer
from .models import Orders, Cones
from datetime import datetime
import json
import pytz


# Create your views here.
@api_view(['POST'])
def delivered(request):
    try:
        query = Orders.objects.get(
                id=request.data['order']
                )
        setattr(query,
                'timeDelivered',
                datetime.now(pytz.timezone('US/Mountain'))
                )
        query.save()
    except KeyError:
        return Response({'error': 'BAD REQUEST'})
    except Exception as err:
        return Response({'error': str(err)})

    return Response({'Response': 'UPDATE_CONFIRMATION'})


@api_view(['POST'])
def new(request):
    try:
        cones = []
        for data in request.data['cones']:
            cone = Cones.objects.create(
                        cone=data['cone'],
                        iceCream=[data['iceCream']],
                        toppings=[data['toppings']],
                        cost=data['cost'],
                        )
            cones.append(cone.id)
        order = Orders.objects.create(
                userID=request.data['userID'],
                droneID=[request.data['droneID']],
                location=request.data['location'],
                timeOrdered=datetime.now(pytz.timezone('US/Mountain')),
                cones=cones
                )
        return Response({'success': f"ORDER: #{order.id}"})
    except KeyError:
        return Response({'error': 'BAD REQUEST'})
    except Exception as err:
        return Response({'error': str(err)})


@api_view(['POST'])
def delete(request):
    try:
        order = Orders.objects.get(id=request.data['order'])
        for cone in order.cones:
            Cones.objects.get(id=cone).delete()
        Orders.objects.get(id=request.data['order']).delete()
        return Response({'success': f"ORDER: #{request.data['order']} DELETED"})
    except KeyError:
        return Response({'error': 'BAD REQUEST'})
    except Exception as err:
        return Response({'error': str(err)})


@api_view(['GET'])
def order_search(request):
    try:
        query = Orders.objects.get(id=request.query_params['order'])
        cones = []
        for cone in query.cones:
            cones.append(Cones.objects.get(id=cone))
        query.cones = cones
        res = OrdersSerializer(query, many=False)
        return Response(res.data)
    except KeyError:
        return Response({'error': 'BAD REQUEST'})
    except Exception as err:
        return Response({'error': str(err)})
