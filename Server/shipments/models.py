from django.db import models
from Users.models import CustomUser
from Orders.models import Order
from django.utils import timezone

from django.core.exceptions import ValidationError


# Create your models here.
class Shipment(models.Model):
    CARRIER_CHOICES = [
        ("UPS", "UPS"),
        ("FedEx", "FedEx"),
        ("DHL", "DHL"),
        ("Aramex", "Aramex"),
    ]

    order = models.OneToOneField(
        Order, on_delete=models.PROTECT, related_name="shipment"
    )
    is_delivered = models.BooleanField(default=False)
    is_shipped = models.BooleanField(default=False)
    carrier = models.CharField(max_length=50, choices=CARRIER_CHOICES)
    estimated_delivery_date = models.DateField()
    # both will be edited upon is_shipped and is_delivered
    shipping_date = models.DateField(blank=True, null=True, editable=False)
    actual_delivery_date = models.DateField(null=True, blank=True, editable=False)

    def delete(self, *args, **kwargs):
        if self.order.full_filled:
            # Make sure order is shipped as it's full filled
            if not self.is_delivered:
                self.is_delivered = True
                super().save(*args, **kwargs)
            raise ValidationError("Cannot delete shipment of a full filled order.")
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        # estimated_delivery_date is reasonable
        if self.estimated_delivery_date <= self.order.created_at:
            raise ValidationError(
                "Estimated delivery date must be after the order creation date."
            )

        # set dates automatically else set them back to None
        if self.is_delivered and self.actual_delivery_date is None:
            self.actual_delivery_date = timezone.now()
        else:
            self.actual_delivery_date = None

        if self.is_shipped and self.shipping_date is None:
            self.shipping_date = timezone.now()
        else:
            self.shipping_date = None
        # product is shipped then delivered
        if self.is_delivered and not self.is_shipped:
            raise ValidationError("This product should be shipped before delivery!.")
        # Make sure order is full filled
        if self.is_delivered and self.order.payment.is_paid:
            self.order.is_fulfilled = True
            self.order.save()

        super().save(*args, **kwargs)
