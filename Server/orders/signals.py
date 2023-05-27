from django.utils import timezone
from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver
from .models import Order, OrderItem
from django.core.exceptions import ValidationError
from Cart.models import Cart
from payments.models import Payment
from shipments.models import Shipment


@receiver(pre_save, sender=Order)
def check_cart_item(sender, instance, **kwargs):
    order = instance
    cart = Cart.objects.get(user=order.user)
    if cart.cartitem_set.all().count() == 0:
        raise ValidationError("Cannot place an order with an empty cart.")


@receiver(post_save, sender=Order)
def place_order(sender, instance, created, **kwargs):
    # Create the order
    order = instance
    if created:
        cart = Cart.objects.get(user=order.user)

        # Add the products to the order
        for item in cart.cartitem_set.all():
            product = item.product
            quantity = item.quantity

            # Check if the product quantity is sufficient
            if product.quantity < quantity:
                raise ValidationError(
                    "Cannot add more than the available quantity of this product."
                )

            # Create the order item
            OrderItem.objects.create(order=order, product=product, quantity=quantity)

            # Decrease the product quantity
            product.quantity -= quantity
            product.save()

        # Clear the cart
        cart.cartitem_set.all().delete()

        # get or create to avoid integrity errors
        Payment.objects.get_or_create(order=order)
        Shipment.objects.get_or_create(
            order=order,
            estimated_delivery_date=timezone.now() + timezone.timedelta(days=1),
        )


@receiver(pre_delete, sender=Order)
def delete_order(sender, instance, **kwargs):
    order = instance

    if order.full_filled:
        raise ValidationError("Cannot delete order while it's fulfilled")

    # set back the original product quantity
    for order_item in order.orderitem_set.all():
        order_item.product.quantity += order_item.quantity
        order_item.product.save()
