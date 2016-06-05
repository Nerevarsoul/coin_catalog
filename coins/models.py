# -*- coding: UTF-8  -*-
from django.core.urlresolvers import reverse
from django.db import models

from accounts.models import User
from core.models import Country, Image


COUNTRY_STATUS = (
    (1, 'Не существующая'),
    (2, 'Существующая'),
)


# Create your models here.

class CatalogCoin(models.Model):
    
    country = models.ForeignKey(Country)
    currency = models.CharField(max_length=50)
    face_value = models.IntegerField()
    metal = models.CharField(max_length=50, blank=True, null=True)
    ruler = models.CharField(max_length=50, blank=True, null=True)
    number = models.CharField(max_length=50, blank=True, null=True)
    circulation = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    catalog_image = models.ManyToManyField(Image)
    slug = models.SlugField(max_length=150)
    
    def __str__(self):
        return "{} {}".format(self.face_value, self.currency)
        
    def get_absolute_url(self):
        return reverse('catalog_detail_coins', args=[self.slug])
    
    
class Coin(models.Model):

    condition = models.CharField(max_length=50, blank=True, null=True)
    year = models.IntegerField()
    mint = models.CharField(max_length=50, blank=True, null=True)
    catalog_coin = models.ForeignKey(CatalogCoin)
    image = models.ManyToManyField(Image)
    available = models.ForeignKey(User, blank=True, null=True,
                                  related_name="user_have")
    needful = models.ForeignKey(User, blank=True, null=True,
                                related_name="user_wish")
    changable = models.ForeignKey(User, blank=True, null=True,
                                  related_name="user_change")

    def __str__(self):
        return "{} {}".format(self.catalog_coin, self.year)
