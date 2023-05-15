from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Order

# force total price to be calculated correctly
@receiver(pre_save, sender=Order)
def calculate_total_price(sender, instance, **kwargs):
    instance.total_price = instance.Product.price * instance.quantity