from django.contrib.admin.views.autocomplete import JsonResponse


def create_account(request):
    return JsonResponse({'Response': 'CREATE_ACCOUNT_CONFIRMATION'})


def delete_account(request):
    return JsonResponse({'Response': 'DELETE_ACCOUNT_CONFIRMATION'})


def edit_account(request):
    return JsonResponse({'Response': 'EDIT_ACCOUNT_CONFIRMATION'})


def get_permissions(request):
    return JsonResponse({'Response': 'ACCOUNT_PERMISSIONS'})


def update_permissions(request):
    return JsonResponse({'Response': 'UPDATE_PERMISSIONS_CONFIRMATION'})
