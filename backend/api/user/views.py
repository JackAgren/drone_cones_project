from django.contrib.admin.views.autocomplete import JsonResponse
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets, mixins, generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from .serializers import UsersSerializer
from .models import CustomUser
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404

# get all users
class UserList(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = CustomUser.objects.all()
    serializer_class = UsersSerializer

# get a specific user
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UsersSerializer

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_users(request):
    try:
        if 'email' in request.query_params:
            query = CustomUser.objects.get(email=request.query_params['email'])
            many = False
        elif 'id' in request.query_params:
            query = CustomUser.objects.get(id=request.query_params['id'])
            many = False
        else:
            query = CustomUser.objects.all()
            many = True
        serialized = UsersSerializer(query, many=many)
        #if serialized.is_valid():
        return Response({"user": serialized.data})
    except Exception as e:
        return Response({"detail": "Not found."}, status=status.HTTP_400_BAD_REQUEST)
        


@api_view(['POST'])
def create_account(request):
    serializer = UsersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = CustomUser.objects.get(email=request.data['email'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializer.data})
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    user = get_object_or_404(CustomUser, email=request.data['email'])
    if not user.check_password(request.data['password']):
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UsersSerializer(instance=user)
    return Response({'token': token.key, "user": serializer.data})

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response(f"{request.user.email} has a valid token")

@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_account(request):
    try:
        user = get_object_or_404(CustomUser, email=request.data['email'])
        user.delete()
        return Response({"deleted": request.data['email']})
    except CustomUser.DoesNotExist as e:
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)


def edit_account(request):
    return JsonResponse({'Response': 'EDIT_ACCOUNT_CONFIRMATION'})


def get_permissions(request):
    return JsonResponse({'Response': 'ACCOUNT_PERMISSIONS'})


def update_permissions(request):
    return JsonResponse({'Response': 'UPDATE_PERMISSIONS_CONFIRMATION'})
