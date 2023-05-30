from django import forms
from .models import CustomUser, Gender
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm


class CustomUserChangeForm(UserChangeForm):
    is_dealer = forms.BooleanField(required=False)
    profile_picture = forms.ImageField(required=False)
    email = forms.EmailField(max_length=254, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    first_name = forms.CharField(max_length=30, required=False)
    username = forms.CharField(max_length=30, required=False)

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "is_dealer",
            "profile_picture",
        ]
# TODO: handle saving fields that changed only.
    def save(self, commit=True):
        user = super().save(commit=False)

        # Only save fields that have values
        for field in self.Meta.fields:
            value = self.cleaned_data.get(field)
            if value is not None:
                setattr(user, field, value)

        if commit:
            user.save()
        return user


class CustomUserCreationForm(UserCreationForm):
    is_dealer = forms.BooleanField(required=False)
    profile_picture = forms.ImageField(required=False)
    email = forms.EmailField(max_length=254, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    gender = forms.ChoiceField(
        choices=[(gender.name, gender.value) for gender in Gender], required=True
    )

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "gender",
            "is_dealer",
            "profile_picture",
        ]
