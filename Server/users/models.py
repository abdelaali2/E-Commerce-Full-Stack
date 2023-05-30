import uuid
from enum import Enum
from django.db import models
from enumfields import EnumField
from django.contrib.auth.models import AbstractUser


def scramble_uploaded_filename(instance, filename):
    extension = filename.split(".")[-1]
    return "{}.{}".format(uuid.uuid4(), extension)


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"


class CustomUser(AbstractUser):
    is_dealer = models.BooleanField(default=False, blank=True)
    profile_picture = models.ImageField(
        upload_to=scramble_uploaded_filename, blank=True, null=True
    )
    gender = EnumField(Gender, max_length=10, default=Gender.MALE)
