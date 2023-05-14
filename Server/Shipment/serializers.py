from rest_framework import serializers
from .models import Shipment
from Cart.serializers import CartSerializer
from Payment.serializers import PaymentSerializer


class ShipmentSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer()
    cart = CartSerializer(read_only=True)

    class Meta:
        model = Shipment
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        user = self.context["request"].user
        if instance.user != user:
            data["payment"] = None
            data["cart"] = None
        return data
