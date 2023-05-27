from django.shortcuts import get_object_or_404
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.response import Response

from Product.models import Product
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.sessions.models import Session
from Users.models import CustomUser


def get_user_by_sessionid(sessionid):
    if not sessionid:
        raise ValueError("Bad request")

    try:
        session = Session.objects.get(pk=sessionid)
        user = get_object_or_404(
            CustomUser, pk=session.get_decoded().get("_auth_user_id")
        )
        return user
    except Exception:
        raise ValueError("Bad request")


@api_view(["GET"])
@permission_classes([AllowAny])
def cart_detail(request):
    user_id = get_user_by_sessionid(request.META.get("HTTP_X_SESSIONID"))
    cart = get_object_or_404(Cart, user=user_id)
    serializer = CartSerializer(cart)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@ensure_csrf_cookie
def add_to_cart(request):
    print("add_to_cart")
    user = request.user
    try:
        cart = Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=user)
    serializer = CartItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(cart=cart)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(["GET"])
@permission_classes([AllowAny])
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
        user_id = get_user_by_sessionid(request.META.get("HTTP_X_SESSIONID"))
    except Exception as e:
        return Response({"error": str(e)}, status=400)

    cart = get_object_or_404(Cart, user=user_id)
    cart_items = cart.cartitem_set.all()
    serializer = CartItemSerializer(cart_items, many=True)
    return Response(serializer.data)


@api_view(["PUT", "DELETE"])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def cart_item_detail(request, item_id):
    try:
        user_id = get_user_by_sessionid(request.META.get("HTTP_X_SESSIONID"))
    except Exception as e:
        return Response({"error": str(e)}, status=400)

    cart = get_object_or_404(Cart, user=user_id)
    cart_item = get_object_or_404(CartItem, pk=item_id, cart=cart)

    if request.method == "PUT":
        cart_item.quantity = request.data.get("quantity", cart_item.quantity)
        product = get_object_or_404(Product, pk=request.data.get("product"))

        data = {
            "id": cart_item.id,
            "product": {
                "id": product.id,
                "name": product.name,
                "price": product.price,
            },
            "quantity": cart_item.quantity,
        }
        serializer = CartItemSerializer(
            cart_item,
            data=data,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == "DELETE":
        cart_item.delete()
        return Response(status=204)
