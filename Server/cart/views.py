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
    try:
        user_obj = get_user_by_sessionid(request.COOKIES.get("sessionid"))
    except Exception as e:
        return Response(status=status.HTTP_403_FORBIDDEN)
    cart = Cart.objects.get(user=user_obj.id)

    serializer = CartItemSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save(cart=cart)
        except IntegrityError as e:
            return Response({"error": "IntegrityError: {}".format(str(e))}, status=400)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


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
