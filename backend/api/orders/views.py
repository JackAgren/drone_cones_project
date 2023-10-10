from os import walk
from django.contrib.admin.views.autocomplete import JsonResponse

# Create your views here.
def update(request):
    return JsonResponse({'Response': 'UPDATE_CONFIRMATION'}) 

def new(request):
    return JsonResponse({'Response': 'NEW_CONFIRMATION'}) 

def delete(request):
    return JsonResponse({'Response': 'DELETE_CONFIRMATION'}) 

def order_search(request):
    return JsonResponse({'Response': 'ORDERN'}) 
