from rest_framework.decorators import api_view, authentication_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import InventorySerializer
from .models import Inventory
from datetime import datetime


@api_view(['GET'])
def get_inventory(request):
    if request.query_params:
        try:
            query = Inventory.objects.get(description=request.query_params['description'])
            res = InventorySerializer(query, many=False)
        except Exception as err:
            return Response({'error': str(err)})
    else:
        queryset = Inventory.objects.all()
        res = InventorySerializer(queryset, many=True)
        if not queryset:
            return Response({'error': 'Inventory empty.'})

    return Response(res.data)


# ./add/description=<description>&cost=<cose-of-unit>&quantity=<quantity>
@api_view(['POST'])
def add_inventory(request):
    try:
        quantity = request.data['quantity'] if request.data['quantity'] else 0
        dateFilled = request.data['dateFilled'] if request.data['dateFilled'] else datetime.now()
        Inventory.objects.create(description=request.data['description'], salesPrice=request.data['salesPrice'], costPerUnit=request.data['costPerUnit'], quantity=quantity, dateFilled=dateFilled)
        return Response({'success': 'ADDED'})
    except KeyError:
        return Response({'error': 'BAD REQUEST'})
    except Exception as err:
        return Response({'error': str(err)})


# ./remove/description=<description>&cost=<cose-of-unit>&quantity=<quantity>
@api_view(['POST'])
def remove_inventory(request):
    try:
        query = Inventory.objects.get(description=request.request.data['description']).delete()
        return Response({'success': 'DELETED'})
    except KeyError:
        return Response({'error': 'BAD REQUEST'})
    except Exception as err:
        return Response({'error': str(err)})


# ./increment/description=<description>&num_increment=<number-to-add>
@api_view(['POST'])
def increment_inventory(request):
    try:
        query = Inventory.objects.get(description=request.data['description'])
        setattr(query, 'quantity', query.quantity + request.data['amount'])
        setattr(query, 'dateFilled', datetime.now())
        query.save()
        return Response({'success': f"{request.data['amount']} units added to {request.data['description']}"})
    except KeyError:
        return Response({'error': 'BAD REQUEST'})
    except Exception as err:
        return Response({'error': str(err)})


# ./decrement/description=<description>&num_increment=<number-to-remove>
@api_view(['POST'])
def decrement_inventory(request):
    try:
        query = Inventory.objects.get(description=request.data['description'])
        setattr(query, 'quantity', query.quantity - request.data['amount'])
        query.save()
        return Response({'success': f"{request.data['amount']} units removed from {request.data['description']}"})
    except KeyError:
        return Response({'error': 'BAD REQUEST'})
    except Exception as err:
        return Response({'error': str(err)})
