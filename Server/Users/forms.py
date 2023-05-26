from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    is_dealer = forms.BooleanField(required=False)
    profile_picture = forms.ImageField(required=False)
    email = forms.EmailField(max_length=254, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    first_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "is_dealer",
            "profile_picture",
        ]
