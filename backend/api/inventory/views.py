# Create your views here.
from rest_framework.decorators import api_view
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
        Inventory.objects.create(description=request.data['description'], salesPrice=request.data['salesPrice'], costPerUnit=request.data['costPerUnit'], quantity=quantity, dateFilled=datetime.now())
        return Response({'success': 'ADDED'})
    except Exception as err:
        return Response({'error': str(err)})


# ./remove/description=<description>&cost=<cose-of-unit>&quantity=<quantity>
@api_view(['POST'])
def remove_inventory(request):
    try:
        query = Inventory.objects.get(description=request.query_params['description']).delete()
        return Response({'success': 'DELETED'})
    except Exception as err:
        return Response({'error': str(err)})


# ./increment/description=<description>&num_increment=<number-to-add>
@api_view(['POST'])
def increment_inventory(request):
    try:
        query = Inventory.objects.get(description=request.GET['description'])
        setattr(query, 'quantity', query.quantity + request.data['amount'])
        query.save()
        return Response({'success': f"{request.data['amount']} units added to {request.query_params['description']}"})
    except Exception as err: 
        return Response({'error': str(err)})


# ./decrement/description=<description>&num_increment=<number-to-remove>
def decrement_inventory(request):
    try:
        query = Inventory.objects.get(description=request.GET['description'])
        setattr(query, 'quantity', query.quantity - request.data['amount'])
        query.save()
        return Response({'success': f"{request.data['amount']} units removed from {request.query_params['description']}"})
    except Exception as err: 
        return Response({'error': str(err)})
