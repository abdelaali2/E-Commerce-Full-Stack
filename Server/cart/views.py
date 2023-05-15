from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer

@api_view(['GET', 'POST'])
def cart_list(request):
    if request.method == 'GET':
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def cart_detail(request, cart_id):
    try:
        Cart = Cart.objects.get(pk=cart_id)
    except Cart.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = CartSerializer(Cart)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CartSerializer(Cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        Cart.delete()
        return Response(status=204)

@api_view(['POST'])
def add_to_cart(request):
    serializer = CartItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT', 'DELETE'])
def cart_item_detail(request, item_id):
    try:
        item = CartItem.objects.get(pk=item_id)
    except CartItem.DoesNotExist:
        return Response(status=404)

    if request.method == 'PUT':
        serializer = CartItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)