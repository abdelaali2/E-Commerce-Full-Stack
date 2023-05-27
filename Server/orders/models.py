from django.db import models
from Users.models import CustomUser
from Product.models import Product


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    full_filled = models.BooleanField(default=False)

    def total_price(self):
        total = sum(
            item.quantity * (item.product.price * (1 - item.product.discount))
            for item in self.orderitem_set.all()
        )
        return total

    def __str__(self):
        return f"Order of: {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.order.user.username} - {self.product.name} - {self.quantity}"
