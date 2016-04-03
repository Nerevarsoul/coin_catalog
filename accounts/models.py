from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models

from core.models import Country


# Create your models here.
class User(AbstractUser):

    avatar = models.ImageField(upload_to='profile_images', blank=True, null=True)
    address = models.ForeignKey("Address", blank=True, null=True)

    def __unicode__(self):
        return self.username

    
class Address(models.Model):

    country = models.ForeignKey(Country, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    building = models.IntegerField(blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return "{}, {}".format(self.country, self.city)
