from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .models import Order
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from utils.get_user_id import get_user_by_sessionid
from rest_framework import status


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def order(request):
    # TODO: got_list_or_404
    user_obj = request.user
    order = get_object_or_404(Order, user=user_obj.id)
    serializer = OrderSerializer(order)
    return Response(serializer.data)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_order(request):
    # TODO: got_list_or_404 delete specific order
    try:
        user_obj = get_user_by_sessionid(request.COOKIES.get("sessionid"))
    except Exception as e:
        return Response(status=status.HTTP_403_FORBIDDEN)

    order = get_object_or_404(Order, user=user_obj.id)
    order.shipment.delete()
    order.payment.delete()
    order.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
