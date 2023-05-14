from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from Cart.models import Cart
from .models import Shipment
from .serializers import ShipmentSerializer


# Create your views here.


class ShipmentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ShipmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Shipment.objects.filter(user=self.request.user).select_related("cart")

    def perform_create(self, serializer):
        cart = Cart.objects.get_or_create(user=self.request.user)[0]
        serializer.save(user=self.request.user, cart=cart)


class ShipmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShipmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Shipment.objects.filter(user=self.request.user).select_related("cart")

    def perform_update(self, serializer):
        cart = Cart.objects.get_or_create(user=self.request.user)[0]
        serializer.save(user=self.request.user, cart=cart)
