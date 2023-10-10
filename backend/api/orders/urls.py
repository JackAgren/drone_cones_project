from django.urls import include, path
from .import views

urlpatterns =[
    path('order_search', views.order_search, name='order_search'),
    path('new', views.new, name='new'),
    path('delete', views.delete, name='delete'),
    path('update', views.update, name='update'),
]
