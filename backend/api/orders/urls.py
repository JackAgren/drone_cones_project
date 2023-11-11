from django.urls import include, path
from .import views

urlpatterns = [
    path('order_search', views.order_search, name='order_search'),
    path('add', views.add, name='new'),
    path('remove', views.remove, name='delete'),
    path('delivered', views.delivered, name='update'),
    path('drone_earnings', views.get_drone_earnings, name='drone_earnings'),
    path('company_balance', views.get_company_balance, name='company_balance')
]
