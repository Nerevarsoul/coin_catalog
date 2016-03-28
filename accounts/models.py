from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from core.models import Country


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")

    avatar = models.ImageField(upload_to='profile_images', blank=True, null=True)
    address = models.ForeignKey("Address", blank=True, null=True)

    def __unicode__(self):
        return self.user.username

    
class Address(models.Model):

    country = models.ForeignKey(Country, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    building = models.IntegerField(blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return "{}, {}".format(self.country, self.city)
