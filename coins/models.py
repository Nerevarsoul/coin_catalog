# -*- coding: UTF-8  -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class CatalogCoins(models.Model):
    
    country = models.CharField(max_length=50)
    currency = models.CharField(max_length=50)
    face_value = models.IntegerField()
    metal = models.CharField(max_length=50, blank=True)
    ruler = models.CharField(max_length=50, blank=True)
    number = models.CharField(max_length=50, blank=True)
    circulation = models.IntegerField(blank=True)
    description = models.TextField(blank=True)


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


class Country(models.Model):

    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")

    avatar = models.ImageField(upload_to='profile_images', blank=True)
    address = models.TextField(blank=True)

    