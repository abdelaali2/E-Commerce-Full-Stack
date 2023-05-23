from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from Product.models import Product
from Users.models import CustomUser


# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True)
    rating = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(5, message="Rating cannot be greater than 5."),
            MinValueValidator(0, message="Rating cannot be less than 0."),
        ],
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
