from django.contrib.admin.views.autocomplete import JsonResponse


def add(request):
    return JsonResponse({'Response': 'NEW_PERMISSION_CHANGE_CONFIRMATION'})


def delete(request):
    return JsonResponse({'Response': 'DELETE CONFIRMATION'})


def approve(request):
    return JsonResponse({'Response': 'APPROVE_REQUEST'})


def get_permission_request(request):
    return JsonResponse({'Response': 'PERMISSION_CHANGE_REQUEST'})
