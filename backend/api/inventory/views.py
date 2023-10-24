# Create your views here.
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import View
from rest_framework import viewsets, mixins, generics
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .serializers import InventorySerializer
from .models import Inventory

# ./get_inv?description=<description>
@csrf_exempt
def inv_api(request, pk):
    if request.method == 'GET':
        items = Inventory.objects.get(pk=pk)
        serializer = InventorySerializer(items)
        return JsonResponse(serializer.data, safe=False)





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
