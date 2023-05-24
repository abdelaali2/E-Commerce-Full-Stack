from django.db import models
from Users.models import CustomUser

# TODO: decrease quantity whenever order is initialized
# TODO: clean cart

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    Product = models.ForeignKey("Product.Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.Product} - {self.quantity}"
