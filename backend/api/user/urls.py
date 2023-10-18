from django.urls import include, path
from .import views

urlpatterns = [
    path('create_account', views.create_account, name='create_account'),
    path('delete_account', views.delete_account, name='delete_account'),
    path('edit_account', views.edit_account, name='edit_account'),
    path('get_permissions', views.get_permissions, name='get_permissions'),
    path('update_permissions', views.update_permissions, name='update_permissions'),
]