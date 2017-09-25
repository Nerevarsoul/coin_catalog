from django.contrib.auth.models import AbstractUser
from django.db import models

from core.models import Image


class User(AbstractUser):

    avatar = models.ForeignKey(Image, blank=True, null=True)

    def __str__(self):
        return self.username
