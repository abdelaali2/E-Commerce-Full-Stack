from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.response import Response

from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from rest_framework.permissions import IsAuthenticated
from utils.get_user_id import get_user_by_sessionid
from rest_framework import status
from Cart.models import CartItem
from Product.models import Product


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def cart_detail(request):
    try:
        user_obj = get_user_by_sessionid(request.COOKIES.get("sessionid"))
    except Exception as e:
        return Response(status=status.HTTP_403_FORBIDDEN)

    cart = get_object_or_404(Cart, user=user_obj.id)
    serializer = CartSerializer(cart)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@ensure_csrf_cookie
def add_to_cart(request):
    user_obj = request.user
    cart = Cart.objects.get(user=user_obj.id)

    product = request.data.get("product")
    quantity = request.data.get("quantity")

    if not product:
        return Response({"error": "Product field is required."}, status=400)

    if not quantity:
        return Response({"error": "Quantity field is required."}, status=400)

    product = get_object_or_404(Product, pk=product)
    try:
        cartItem = CartItem.objects.get(product=product, cart=cart)
    except Exception:
        try:
            CartItem.objects.create(
                cart=cart, product=product, quantity=quantity
            ).save()
        except Exception as e:
            return Response(
                {"error": e, "id": str(product.id)}, status=status.HTTP_400_BAD_REQUEST
            )
        return Response(status=201)

    cartItem.quantity += quantity
    try:
        cartItem.save()
    except Exception as e:
        return Response(
            {"error": e, "id": str(product.id)}, status=status.HTTP_400_BAD_REQUEST
        )
    return Response(status=201)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def cart_item_list(request):
    """
    Response for cart_item_list

    [
     {
         id: number
        {
            product model
        }
         quantity: number
     }
    ]
    """
    try:
        user_obj = get_user_by_sessionid(request.COOKIES.get("sessionid"))
    except Exception as e:
        return Response(status=status.HTTP_403_FORBIDDEN)

    cart = get_object_or_404(Cart, user=user_obj)
    cart_items = cart.cartitem_set.all()
    serializer = CartItemSerializer(cart_items, many=True)
    return Response(serializer.data)


@api_view(["PUT", "DELETE"])
@permission_classes([IsAuthenticated])
@ensure_csrf_cookie
def cart_item_detail(request, id):
    try:
        user_obj = get_user_by_sessionid(request.COOKIES.get("sessionid"))
    except Exception as e:
        return Response(status=status.HTTP_403_FORBIDDEN)

    cart = get_object_or_404(Cart, user=user_obj.id)
    cart_item = get_object_or_404(CartItem, pk=id, cart=cart)
    if request.method == "PUT":
        # product is read only so you will never be able to adjust it from here
        serializer = CartItemSerializer(
            cart_item,
            data=request.data,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == "DELETE":
        cart_item.delete()
        return Response(status=204)
