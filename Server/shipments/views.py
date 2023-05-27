from rest_framework.decorators import api_view
from utils.get_user_id import get_user_by_sessionid
from rest_framework import status
from rest_framework.views import Response
from django.shortcuts import get_object_or_404
from shipments.models import Shipment
from shipments.serializers import ShipmentSerializer

# Create your views here.
@api_view(["PUT"])
def edit_shipment(request, pk):
    try:
        user_obj = get_user_by_sessionid(request.COOKIES.get("sessionid"))
    except Exception as e:
        return Response(status=status.HTTP_403_FORBIDDEN)

    shipment = get_object_or_404(Shipment, pk=pk)

    # Ensure that this shipment is associated with an order that belongs to a user with the current session id
    get_object_or_404(Shipment, user=user_obj, shipment__id=shipment.id)

    serializer = ShipmentSerializer(shipment, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
