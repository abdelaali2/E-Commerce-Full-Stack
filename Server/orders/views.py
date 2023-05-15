from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Order
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


@api_view(['GET'])
@authentication_classes([TokenAuthentication,SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def order_list(request):    
    print(request.user)
    user = request.user
    orders = Order.objects.filter(user=user)
    serializer = OrderSerializer(orders, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@authentication_classes([TokenAuthentication,SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def order_detail(request, pk):
    user = request.user
    order = get_object_or_404(Order, pk=pk,user=user)
    serializer = OrderSerializer(order)
    return JsonResponse(serializer.data)

@api_view(['POST'])
@csrf_exempt
def order_create(request):
    print(">>",request.POST)
    serializer = OrderSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@api_view(['PUT', 'PATCH'])
@csrf_exempt
def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    serializer = OrderSerializer(order, data=request.POST, partial=True)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

@api_view(['DELETE'])
@csrf_exempt
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return JsonResponse({'message': 'Order deleted successfully'})