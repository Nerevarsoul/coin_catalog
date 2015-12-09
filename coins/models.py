# -*- coding: UTF-8  -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


COUNTRY_STATUS = (
    (1, 'Не существующая'),
    (2, 'Существующая'),
)

# Create your models here.
class CatalogCoins(models.Model):
    
    country = models.ForeignKey("Country")
    currency = models.CharField(max_length=50)
    face_value = models.IntegerField()
    metal = models.CharField(max_length=50, blank=True)
    ruler = models.CharField(max_length=50, blank=True)
    number = models.CharField(max_length=50, blank=True)
    circulation = models.IntegerField(blank=True)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return "{} {}".format(self.face_value, self.currency)


class Coins(models.Model):

    condition = models.CharField(max_length=50, blank=True)
    year = models.IntegerField()
    mint = models.CharField(max_length=50, blank=True)
    catalog_coin = models.ForeignKey(CatalogCoins)
    available = models.ForeignKey(User, blank=True, 
        related_name="user_have")
    needful = models.ForeignKey(User, blank=True, 
        related_name="user_wish")
    changable = models.ForeignKey(User, blank=True, 
        related_name="user_change")

    def __unicode__(self):
        return "{} {}".format(self.catalog_coin, self.year)


class Country(models.Model):

    name = models.CharField(max_length=50)
    status = models.IntegerField(choices=COUNTRY_STATUS)

    def __unicode__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")

    avatar = models.ImageField(upload_to='profile_images', blank=True)
    address = models.ForeignKey("Address", blank=True)

    def __unicode__(self):
        return self.user.username

    
class Address(models.Model):

    country = models.ForeignKey(Country, blank=True)
    city = models.CharField(max_length=50, blank=True)
    street = models.CharField(max_length=50, blank=True)
    building = models.IntegerField(blank=True)
    index = models.IntegerField(blank=True)

    def __unicode__(self):
        return "{}, {}".format(self.country, self.city)
