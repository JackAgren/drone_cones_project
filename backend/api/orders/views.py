from rest_framework.decorators import api_view, authentication_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import OrdersSerializer
from .models import Orders, Cones
from datetime import datetime
import pytz


# Create your views here.
@api_view(['POST'])
def delivered(request):
    '''
    ** Updates time delivered to time when function was called **
    .orders/delivered

    BODY:
        { "order": <ORDER NUMBER> }
    '''
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

    return Response({'success': 'UPDATE SUCCESS'})


@api_view(['POST'])
def add(request):
    '''
    ./orders/add
    BODY:
    {
        "cones": [
            {
            "cone": <CONE TYPE>: String,
            "iceCream": <ICE CREAM>: String,
            "toppings": [<TOPPINGS>: String,...],
            "cost": <COST>: Float
            },
            ...
            ],
        "userID": <USERID>: Integer,
        "droneID": [<DRONEID>: Integer, ...],
        "location": <LOCATIONS>: String
    }

    '''
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
                droneID=request.data['droneID'],
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
def remove(request):
    '''
    ./orders/remove
    {
    }
    '''
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
    '''

    '''
    try:
        if 'order' in request.query_params:
            query = Orders.objects.all().filter(id=request.query_params['order'])
        elif 'userID' in request.query_params:
            query = Orders.objects.all().filter(userID=request.query_params['userID'])
        elif 'droneID':
            query = Orders.objects.all().filter(userID=request.query_params['droneID'])
        elif 'location':
            query = Orders.objects.all().filter(userID=request.query_params['location'])

        for order in query:
            cones = []
            for cone in order.cones:
                cones.append(Cones.objects.get(id=cone))
            order.cones = cones
        res = OrdersSerializer(query, many=True)
        return Response(res.data)
    except KeyError:
        return Response({'error': 'BAD REQUEST'})
    except Exception as err:
        return Response({'error': str(err)})
