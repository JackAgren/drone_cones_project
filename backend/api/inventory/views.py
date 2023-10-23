# Create your views here.
from django.contrib.admin.views.autocomplete import JsonResponse
from django.contrib.auth.mixins import PermissionRequiredMixin


# ./get_inv?description=<description>
def get_inventory(request):
    r = request.GET
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
