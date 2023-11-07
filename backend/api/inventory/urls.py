from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .import views

app_name = 'inventory'
urlpatterns = [
    path('inventory_search', views.inventory_search, name='list'),
    path('update_item', views.update_item, name='update_item'),
    path('add', views.add_inventory, name='add_inventory'),
    path('remove', views.remove_inventory, name='remove_inventory'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
