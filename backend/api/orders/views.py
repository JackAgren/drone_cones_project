from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from user.models import CustomUser
from drone_operator.models import DroneInfo
from .serializers import OrdersSerializer, NewOrderSerializer
from .models import Orders, Cones
from inventory.models import Inventory
from datetime import datetime
from django.shortcuts import get_object_or_404, get_list_or_404
import pytz


@api_view(["POST"])
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


@api_view(["POST"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def add(request):
    '''
    ./orders/add
    BODY:
    {
        "cones": [
            {
            "cone": <CONE TYPE>: String,
            "iceCream": [<ICE CREAM>: String,...],
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
    serializer = NewOrderSerializer(data=request.data)
    if serializer.is_valid():
        cones = []
        total = 0
        
        # Check current stock of ordered icecream flavors
        for cone in request.data["cones"]:
            outOfStock = []
            for iceCream in cone['iceCream']:
                item = get_object_or_404(Inventory, description=iceCream)
                if item.quantity <= 0:
                    outOfStock.append(item.description)
                else:
                    setattr(item, 'quantity', item.quantity-1)
                    item.save()
            if not len(outOfStock) == 0:
                return Response({ 'outofstock': outOfStock })

            id = Cones.objects.create(
                    toppings=cone['toppings'],
                    iceCream=cone['iceCream'],
                    cost=cone['cost'],
                    cone=cone['cone']
                    ).id
            cones.append(id)
            total += cone['cost']

        userID = get_object_or_404(CustomUser, email=request.data['userID'])
        droneID = get_object_or_404(DroneInfo, id=request.data['droneID'])
        order = Orders.objects.create(
                userID=userID,
                droneID=droneID,
                location=request.data['location'],
                timeOrdered=datetime.now(pytz.timezone('US/Mountain')),
                cones=cones,
                total=total
                )
        return Response({'success': f"ORDER: #{order.id}"})
    return Response(serializer.errors, status=400)


@api_view(["POST"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
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


@api_view(["GET"])
def order_search(request):
    '''

    '''
    try:
        if 'order' in request.query_params:
            query = Orders.objects.all().filter(id=request.query_params['order'])
        elif 'userID' in request.query_params:
            query = Orders.objects.all().filter(userID=get_object_or_404(CustomUser, email=request.query_params['userID']))
        elif 'droneID':
            query = Orders.objects.all().filter(droneID=get_object_or_404(DroneInfo, id=request.query_params['droneID']))
        elif 'location':
            query = Orders.objects.all().filter(location=request.query_params['location'])

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


@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_drone_earnings(request):
    if 'droneID' in request.query_params:
        drone = get_object_or_404(DroneInfo, id=request.query_params["droneID"])
        orders = get_list_or_404(Orders, droneID=drone)
        earnings = 0
        for order in orders:
            earnings += order.total * .10
        return Response({'earnings': f"{earnings}"})
    return Response({'error': "BAD REQUEST"}, status=400)

@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_company_balance(request):
    orders = get_list_or_404(Orders)
    inventory = get_list_or_404(Inventory)
    earnings = 0
    expenses = 0
    for order in orders:
        earnings += order.total

    for item in inventory:
        expenses += item.costPerUnit * item.quantity

    return Response({
        "earnings": earnings,
        "expenses": expenses,
        "balance": earnings - expenses
        })
