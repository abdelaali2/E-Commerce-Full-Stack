from django.urls import path
from .views import *

urlpatterns = [
    path("carts/", cart_list, name="cart-list"),
    path("carts/<int:cart_id>/", cart_detail, name="cart-detail"),
    path("cart-items/", add_to_cart, name="add-to-cart"),
    path("carts/<int:cart_id>/items/", cart_item_list),
    path("cart-items/<int:item_id>/", cart_item_detail, name="cart-item-detail"),
]
