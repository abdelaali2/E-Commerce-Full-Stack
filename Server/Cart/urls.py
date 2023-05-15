from django.urls import path
from . import views

urlpatterns = [
    path('carts/', views.cart_list, name='cart-list'),
    path('carts/<int:cart_id>/', views.cart_detail, name='cart-detail'),
    path('cart-items/', views.add_to_cart, name='add-to-cart'),
    path('cart-items/<int:item_id>/', views.cart_item_detail, name='cart-item-detail'),
]