# Create your views here.
from django.contrib.admin.views.autocomplete import JsonResponse

def get_inventory(request):
    return JsonResponse({ 'Response': 'INVENTORY_GOES_HERE' })

def add_inventory(request):
    return JsonResponse({ 'Response': 'ADD CONFIRMATION' })
    
def remove_inventory(request):
    return JsonResponse({ 'Response': 'REMOVE CONFIRMATION' })

def increment_inventory(request):
    return JsonResponse({ 'Response': 'NEW INVENTORY' })

def decrement_inventory(request):
    return JsonResponse({ 'Response': 'NEW INVENTORY' })
