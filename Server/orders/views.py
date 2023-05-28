from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from .models import Order
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import ensure_csrf_cookie


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def order(request):
    user_obj = request.user
    order = get_list_or_404(Order, user=user_obj.id)
    serializer = OrderSerializer(order, many=True)
    return Response(serializer.data)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
@ensure_csrf_cookie
def delete_order(request, pk):
    user_obj = request.user
    order = get_object_or_404(Order, pk=pk, user=user_obj.id)
    order.shipment.delete()
    order.payment.delete()
    order.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@ensure_csrf_cookie
def create_order(request):
    user_obj = request.user
    order = Order(user=user_obj)
    try:
        order.save()
    except Exception as e:
        return Response(e, status=status.HTTP_400_BAD_REQUEST)
    serializer = OrderSerializer(order)
    return Response(serializer.data, status=status.HTTP_200_OK)
