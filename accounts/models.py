from django.contrib.auth.models import AbstractUser
from django.db import models

from core.models import Country, Image


# Create your models here.
class Address(models.Model):

    country = models.ForeignKey(Country, blank=True, null=True,
                                related_name="country")
    city = models.CharField(max_length=50, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    building = models.IntegerField(blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "{}, {}".format(self.country, self.city)


class User(AbstractUser):

    avatar = models.ForeignKey(Image, blank=True, null=True)
    address = models.ForeignKey(Address, blank=True, null=True)

    def __str__(self):
        return self.username
