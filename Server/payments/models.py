from django.db import models
from Users.models import CustomUser
from Orders.models import Order
from django.core.exceptions import ValidationError
from django.utils import timezone


# Create your models here.
class Payment(models.Model):
    order = models.OneToOneField(
        Order, on_delete=models.PROTECT, related_name="payment"
    )
    is_paid = models.BooleanField(default=False)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, editable=False, blank=True, null=True
    )
    payment_date = models.DateTimeField(blank=True, null=True, editable=False)
    currency = models.CharField(max_length=3, default="EGP")

    def save(self, *args, **kwargs):
        # set the amount for the first time
        if self.amount is None:
            self.amount = self.order.total_price()

        if self.is_paid and self.payment_date is None:
            # set payment date whenever is paid without the ability to edit
            self.payment_date = timezone.now()

        super().save(*args, **kwargs)

        if self.is_paid and self.order.shipment.is_delivered:
            self.order.is_fulfilled = True
            self.order.save()

    def delete(self, *args, **kwargs):
        if self.order.full_filled:
            # Do not delete order if paid
            self.is_paid = True
            raise ValidationError("Cannot delete shipment of a full filled order.")
        super().delete(*args, **kwargs)
