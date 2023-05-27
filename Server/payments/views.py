from django.shortcuts import render
from rest_framework.decorators import api_view
from utils.get_user_id import get_user_by_sessionid
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from payments.models import Payment
from payments.serializers import PaymentsSerializer
from Orders.models import Order

# Create your views here.


@api_view(["PUT"])
def edit_payment(request, pk):
    try:
        user_obj = get_user_by_sessionid(request.COOKIES.get("sessionid"))
    except Exception as e:
        return Response(status=status.HTTP_403_FORBIDDEN)

    payment = get_object_or_404(Payment, pk=pk)

    # Ensure that this payment is associated with an order that belongs to a user with the current session id
    get_object_or_404(Order, user=user_obj, payment__id=payment.id)

    serializer = PaymentsSerializer(payment, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
