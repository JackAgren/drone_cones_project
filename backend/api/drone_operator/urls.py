from django.contrib import admin
from django.urls import include, path
from .import views

app_name = 'drone_operator'
urlpatterns = [
    path('register_drone', views.register_drone, name='register_drone'),
    path('update_status', views.update_status, name='update_status'),
    path('get_status', views.get_status, name='get_status'),
    path('decomission_drone', views.decomission_drone, name='decomission_drone'),
    path('get_all_owned_drones', views.get_all_owned_drones, name='get_all_owned_drones'),
    path('get_delivering_drones', views.get_delivering_drones, name='get_delivering_drones'),
]
