from django.db import models
from Category.models import Category
from Users.models import CustomUser


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.DecimalField(max_digits=2, decimal_places=2, null=True, blank=True)
    category = models.ManyToManyField(Category)
    dealer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    
    @property
    def discounted_price(self):
        if self.discount is not None:
            return self.price * (1 - self.discount)
        else:
            return self.price

    def __str__(self):
        return self.name
