from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from rest_framework.permissions import IsAuthenticated


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def cart_list(request):
    print("cart_list")
    if request.method == "GET":
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    elif request.method == "POST":
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def cart_detail(request, cart_id):
    print("cart_detail")
    try:
        cart = Cart.objects.get(pk=cart_id, user=request.user)
    except cart.DoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == "DELETE":
        cart.delete()
        return Response(status=204)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
def cart_item_list(request, cart_id):
    print("cart_item_list")
    try:
        cart = Cart.objects.get(pk=cart_id, user=request.user)
    except Cart.DoesNotExist:
        return Response(status=404)

    cart_items = cart.cartitem_set.all()
    serializer = CartItemSerializer(cart_items, many=True)
    return Response(serializer.data)


@api_view(["PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def cart_item_detail(request, item_id):
    print("cart_item_detail")
    try:
        item = CartItem.objects.get(pk=item_id)
        if item.cart.user != request.user:
            raise Cart.DoesNotExist
    except CartItem.DoesNotExist:
        return Response(status=404)

    if request.method == "PUT":
        serializer = CartItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == "DELETE":
        item.delete()
        return Response(status=204)
