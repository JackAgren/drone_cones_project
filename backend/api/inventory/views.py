from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import InventorySerializer, DescriptionSerializer 
from .models import Inventory
from datetime import date 
from rest_framework import status
from django.shortcuts import get_object_or_404


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
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_inventory(request):
    '''
    ** Add item matching description  **
    .inventory/add
    BODY:
    {
        "description": "<DESCRIPTION>": String,
        "salesPrice": "<SALESPRICE>": Float,
        "costPerUnit": "<COSTPERUNIT>": Float,
        "quantity": "<QUANTITY>: Integer"
        "category": "<CATEGORY>: String"
    }
    '''
    request.data.update({'quantity': 0})
    request.data.update({'dateFilled': date.today()})
    serializer = InventorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def remove_inventory(request):
    '''
    ** Deletes item matching description  **
    .inventory/remove

    BODY:
    { "description": "<DESCRIPTION>" }
    '''
    serializer = DescriptionSerializer(data=request.data)
    if serializer.is_valid():
        get_object_or_404(Inventory, description=request.data['description']).delete()
        return Response({'success': f"{request.data['description']} deleted."})
    return Response(serializer.errors, status=400)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
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
