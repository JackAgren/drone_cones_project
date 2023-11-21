from django.urls import include, path
from .import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('test_token', views.test_token, name='test_token'),
    path('create_account', views.create_account, name='create_account'),
    path('delete_account', views.delete_account, name='delete_account'),
    path('edit_account', views.edit_account, name='edit_account'),
    path('get_permissions', views.get_permissions, name='get_permissions'),
    path('get_users', views.get_users, name='list'),
    path('create_guest', views.create_guest, name='create_guest'),
    path('delete_guest', views.delete_guest, name='delete_guess'),
]
