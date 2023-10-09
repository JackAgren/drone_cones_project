from django.urls import include, path
from .import views

urlpatterns =[
    path('add', views.add, name='add'),
    path('delete', views.delete, name='delete'),
    path('approve', views.approve, name='approve'),
    path('get_permission_request', views.get_permission_request, name=''),
]
