from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .import views

app_name = 'inventory'
urlpatterns = [
    path('get_inventory', views.InventoryList.as_view(), name='list'),
    path('get_inventory/<str:pk>', views.InventoryDetail.as_view(), name='detail view'),
    #path('get_inventory', views.get_inventory, name='get_inventory'),
    path('increment', views.increment_inventory, name='increment_inventory'),
    path('decrement', views.decrement_inventory, name='decrement_inventory'),
    path('add', views.add_inventory, name='add_inventory'),
    path('remove', views.remove_inventory, name='remove_inventory'),
]

urlpatterns = format_suffix_patterns(urlpatterns)