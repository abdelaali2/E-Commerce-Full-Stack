from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from enumfields import EnumField, Enum

# Create your models here.


class PaymentType(Enum):
    IBAN = "IBAN"
    CREDIT_CARD = "Credit Card"


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_type = EnumField(
        PaymentType, max_length=11, default=PaymentType.CREDIT_CARD
    )
    card_number = models.CharField(max_length=16, blank=True)
    expiration_month = models.CharField(max_length=2, blank=True)
    expiration_year = models.CharField(max_length=4, blank=True)
    cvv = models.CharField(max_length=4, blank=True)
    iban = models.CharField(max_length=34, blank=True)

    def clean(self):
        if self.payment_type == PaymentType.IBAN and not self.iban:
            raise ValidationError({"iban": "IBAN is required for IBAN payment."})
        elif self.payment_type == PaymentType.CREDIT_CARD and (
            not self.card_number
            or not self.expiration_month
            or not self.expiration_year
            or not self.cvv
        ):
            raise ValidationError(
                {
                    "card_number": "Card number is required for credit card payment.",
                    "expiration_month": "Expiration month is required for credit card payment.",
                    "expiration_year": "Expiration year is required for credit card payment.",
                    "cvv": "CVV is required for credit card payment.",
                }
            )

    def __str__(self):
        if self.payment_type == PaymentType.IBAN:
            return f"{self.iban}, '{self.user.username}'"
        else:
            return f"**** **** **** {self.card_number[-4:]}, {self.expiration_month}/{self.expiration_year}, '{self.user.username}'"
