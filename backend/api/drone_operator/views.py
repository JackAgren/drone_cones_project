from django.shortcuts import render
from django.contrib.admin.views.autocomplete import JsonResponse

def register_drone(request):
    return JsonResponse({ 'Response': 'REGISTRATION_CONFIRMATION' })

def update_status(request):
    return JsonResponse({ 'Response': 'UPDATE_CONFIRMATION' })
    
def get_status(request):
    return JsonResponse({ 'Response': 'DRONE_STATUS' })

def decomission_drone(request):
    return JsonResponse({ 'Response': 'DECOMISSION_CONFIRMATION' })

def get_all_owned_drones(request):
    return JsonResponse({ 'Response': 'ALL_OWNED_DRONES' })
