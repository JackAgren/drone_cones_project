from rest_framework.decorators import api_view, authentication_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import InventorySerializer
from .models import Inventory
from datetime import datetime


@api_view(['GET'])
def get_inventory(request):
    '''
    ** Returns item matching description  **
    .inventory/get_inventory?description=<DESCRIPTION>

    ** Returns all items matching description **
    .inventory/get_inventory?description=<DESCRIPTION>
    '''
    try:
        if 'description' in request.query_params:
            query = Inventory.objects.all().filter(description=request.query_params['description'])
        elif 'lessThan' in request.query_params:
            query = Inventory.objects.all().filter(quantity__lt=request.query_params['lessThan'])
        elif 'greaterThan' in request.query_params:
            query = Inventory.objects.all().filter(quantity__gt=request.query_params['greaterThan'])
        res = InventorySerializer(query, many=True)
    except KeyError:
        return Response({'error': 'BAD REQUEST'})
    except Exception as err:
        return Response({'error': str(err)})

    return Response(res.data)


@api_view(['POST'])
def add_inventory(request):
    '''
    ** Add item matching description  **
    .inventory/add

    ** Request Body **
    {
        "description": "<DESCRIPTION>": String,
        "salesPrice": "<SALESPRICE>": Float,
        "costPerUnit": "<COSTPERUNIT>": Float,
        "quantity": "<QUANTITY>": Float | Optional,
    }
    '''
    try:
        quantity = request.data['quantity'] if request.data['quantity'] else 0
        Inventory.objects.create(description=request.data['description'],
                                 salesPrice=request.data['salesPrice'],
                                 costPerUnit=request.data['costPerUnit'],
                                 quantity=quantity, dateFilled=datetime.now())
        return Response({'success': 'ADDED'})
    except KeyError:
        return Response({'error': 'BAD REQUEST'})
    except Exception as err:
        return Response({'error': str(err)})


@api_view(['POST'])
def remove_inventory(request):
    '''
    ** Deletes item matching description  **
    .inventory/remove

    ** Request Body **
    { "description": "<DESCRIPTION>" }
    '''
    try:
        Inventory.objects.get(
                description=request.data['description']).delete()
        return Response({'success': 'DELETED'})
    except KeyError:
        return Response({'error': 'BAD REQUEST'})
    except Exception as err:
        return Response({'error': str(err)})


# .inventory/increment/description=<description>

@api_view(['POST'])
def increment_inventory(request):
    '''
    ** Increment item matching description **
    .inventory/increment

    ** Request Body **
    {
        "description": "<DESCRIPTION>": String,
        "amount": <AMOUNT>: Integer
    }
    '''
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


@api_view(['POST'])
def decrement_inventory(request):
    '''
    ** Decrement item matching description **
    .inventory/increment

    ** Request Body **
    {
        "description": "<DESCRIPTION>": String,
        "amount": <AMOUNT>: Integer
    }
    '''
    try:
        query = Inventory.objects.get(description=request.data['description'])
        setattr(query, 'quantity', query.quantity - request.data['amount'])
        query.save()
        return Response({'success': f"{request.data['amount']} units removed from {request.data['description']}"})
    except KeyError:
        return Response({'error': 'BAD REQUEST'})
    except Exception as err:
        return Response({'error': str(err)})
