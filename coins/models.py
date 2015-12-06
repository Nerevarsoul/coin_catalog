# -*- coding: UTF-8  -*-
from __future__ import unicode_literals

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
	description = models.CharField(max_length=250, blank=True)


class Coins(models.Model):

	condition = models.CharField(max_length=50, blank=True)
	year = models.IntegerField()
	mint = models.CharField(max_length=50, blank=True)
	catalog_coin = models.ForeignKey(CatalogCoins)


class Country(models.Model):

	pass


