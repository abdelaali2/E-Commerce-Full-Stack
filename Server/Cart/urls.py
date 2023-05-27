from django.urls import path
from .views import *

urlpatterns = [
    path("", cart_detail, name="cart"),
    path("add-to-cart/", add_to_cart, name="add-to-cart"),
    path("items/", cart_item_list, name="cart-items"),
    path("cart-item/<int:item_id>/", cart_item_detail, name="cart-item-detail"),
]
