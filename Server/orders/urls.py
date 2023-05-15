from django.urls import path
from . import views

urlpatterns = [
    path('Orders/', views.order_list, name='order_list'),
    path('Orders/<int:pk>/', views.order_detail, name='order_detail'),
    path('Orders/create/', views.order_create, name='order_create'),
    path('Orders/<int:pk>/update/', views.order_update, name='order_update'),
    path('Orders/<int:pk>/delete/', views.order_delete, name='order_delete'),
]