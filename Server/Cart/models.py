from django.db import models
from Product.models import Product
from django.contrib.auth.models import User
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products =  models.ManyToManyField(Product)
    purchase_date = models.DateTimeField(auto_now_add=True)

    @property
    def quantity(self):
        return self.products.count()

    @property
    def price(self):
        total_price = 0
        for product in self.products.all():
            total_price += product.price
        return total_price * self.quantity

    def __str__(self):
        return f"{self.user} user's Cart"