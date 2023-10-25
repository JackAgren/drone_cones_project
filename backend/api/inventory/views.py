# Create your views here.
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets, mixins, generics, status
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from .serializers import InventorySerializer
from .models import Inventory

# ./get_inv?description=<description>

class InventoryList(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    
class InventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


def get_inventory(request): 
    return JsonResponse({ 'Response': 'INVENTORY_GOES_HERE' })

# ./add/description=<description>&cost=<cose-of-unit>&quantity=<quantity>
def add_inventory(request):
    return JsonResponse({ 'Response': 'ADD CONFIRMATION' })
    
# ./remove/description=<description>&cost=<cose-of-unit>&quantity=<quantity>
def remove_inventory(request):
    return JsonResponse({ 'Response': 'REMOVE CONFIRMATION' })


# ./increment/description=<description>&num_increment=<number-to-add>
def increment_inventory(request):
    return JsonResponse({ 'Response': 'NEW INVENTORY' })

# ./decrement/description=<description>&num_increment=<number-to-remove>
def decrement_inventory(request):
    return JsonResponse({ 'Response': 'NEW INVENTORY' })
