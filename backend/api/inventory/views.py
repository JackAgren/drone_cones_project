from rest_framework.decorators import api_view, authentication_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import InventorySerializer
from .models import Inventory
from datetime import datetime


@api_view(['GET'])
def inventory_search(request):
    '''
    ** Returns all inventory **
    .inventory/inventory_search?description=ALL

    ** Returns all items matching description **
    .inventory/inventory_search?description=<DESCRIPTION>
    '''
    try:
        if 'description' in request.query_params:
            if request.query_params['description'] == 'ALL':
                query = Inventory.objects.all()
            else:
                query = Inventory.objects.all().filter(description=request.query_params['description'])
        elif 'category' in request.query_params:
            query = Inventory.objects.all().filter(category=request.query_params['category'])
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
    BODY:
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
                                 category=request.data['category'],
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

    BODY:
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


@api_view(['POST'])
def update_item(request):
    try:
        query = Inventory.objects.get(description=request.data['description'])
        if 'salesPrice' in request.data:
            setattr(query, 'salesPrice', float(request.data['salesPrice']))
        if 'quantity' in request.data:
            setattr(query, 'quantity', query.quantity + float(request.data['quantity']))
        if 'costPerUnit' in request.data:
            setattr(query, 'salesPrice', float(request.data['costPerUnit']))
        if 'category' in request.data:
            setattr(query, 'category', request.data['category'])
        query.save()
        return Response({'success': f"{query.description} updated."})
    except KeyError:
        return Response({'error': 'BAD REQUEST'})
    except Exception as err:
        return Response({'error': str(err)})
