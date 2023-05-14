from django.db import models
from Category.models import Category

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    in_stock = models.BooleanField(default=True)
    entry_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.name
