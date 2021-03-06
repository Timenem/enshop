from django.urls import path
from .views import *

urlpatterns = [
    path('', Monitor, name='main_page'),

    path('add_client', CreateClient.as_view(), name='add_client'),
    path('<int:pk>/update_client', UpdateClient.as_view(), name='update_client'),
    path('<int:pk>/delete_client', DeleteClient.as_view(), name='delete_client'),
    path('<int:pk>/client_orders_list', clientorderslist, name='client_orders_list'),

    path('add_product', CreateProduct.as_view(), name='add_product'),
    path('<int:pk>/update_product', UpdateProduct.as_view(), name='update_product'),
    path('<int:pk>/delete_product', DeleteProduct.as_view(), name='delete_product'),

    path('balance', balance, name='balance'),
    path('order', CreateOrder.as_view(), name='order'),
    path('orders_list', orders_list, name='orders_list'),
    path('<int:pk>/update_order', UpdateOrder.as_view(), name='update_order'),
    path('<int:pk>/delete_order', DeleteOrder.as_view(), name='delete_order'),
]