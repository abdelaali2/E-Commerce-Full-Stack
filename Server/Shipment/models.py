from django.db import models
from django.db import models
from django.contrib.auth.models import User
from Payment.models import Payment
from Cart.models import Cart

# Create your models here.
class Shipment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.address}, {self.city}, {self.state}, {self.country}, {self.zip_code}"
