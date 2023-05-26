import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


def scramble_uploaded_filename(instance, filename):
    extension = filename.split(".")[-1]
    return "{}.{}".format(uuid.uuid4(), extension)


class CustomUser(AbstractUser):
    is_dealer = models.BooleanField(default=False, blank=True)
    profile_picture = models.ImageField(
        upload_to=scramble_uploaded_filename, blank=True, null=True
    )
