import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from core.models import Image


class User(AbstractUser):

    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    avatar = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.username
