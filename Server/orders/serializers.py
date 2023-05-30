from rest_framework import serializers
from .models import OrderItem, Order
from Product.serializers import ProductSerializer
from shipments.serializers import ShipmentSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = ("product", "quantity")


class OrderSerializer(serializers.ModelSerializer):
    order_items = serializers.SerializerMethodField()
    payment_details = serializers.SerializerMethodField()
    shipment_details = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            "id",
            "user",
            "created_at",
            "updated_at",
            "order_items",
            "total_price",
            "payment_details",
            "shipment_details",
        )

    def get_total_price(self, obj):
        return obj.total_price()

    def get_order_items(self, obj):
        order_items = OrderItem.objects.filter(order=obj)
        serialized_order_items = OrderItemSerializer(order_items, many=True).data
        return serialized_order_items

    def get_payment_details(self, obj):
        return {
            "id": obj.payment.id,
            "amount": obj.payment.amount,
            "currency": obj.payment.currency,
            "order_is_paid:": obj.payment.is_paid,
            "payment_date": obj.payment.payment_date,
        }

    def get_shipment_details(self, obj):
        return {
            "carrier": obj.shipment.carrier,
            "is_delivered": obj.shipment.is_delivered,
            "actual_delivery_date": obj.shipment.actual_delivery_date,
            "is_shipped": obj.shipment.is_shipped,
            "shipping_date": obj.shipment.shipping_date,
            "estimated_delivery_date": obj.shipment.estimated_delivery_date,
        }
