from django.urls import include, path
from .import views

urlpatterns = [
    path('order_search', views.order_search, name='order_search'),
    path('add', views.add, name='new'),
    path('remove', views.remove, name='delete'),
    path('delivered', views.delivered, name='update'),
]
