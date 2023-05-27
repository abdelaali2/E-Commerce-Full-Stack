from django.db import models
from Product.models import Product
from Users.models import CustomUser
from django.core.exceptions import ValidationError

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through="CartItem")

    def __str__(self):
        return f"{self.user.username}'s cart"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def save(self, *args, **kwargs):
        if self.quantity > self.product.quantity:
            raise ValidationError(
                "Cannot add more than the available quantity of this product."
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name}"
