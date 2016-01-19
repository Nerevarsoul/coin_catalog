# -*- coding: UTF-8  -*-
from __future__ import unicode_literals

from unidecode import unidecode

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

from .models import CatalogCoins, Country


@receiver(pre_save, sender=CatalogCoins)
def catalog_get_slug(sender, instance, **kwargs):
    instance.slug = slugify("{} {} {} {}".format(instance.face_value, 
                                                 unidecode(instance.currency), 
                                                 instance.circulation, 
                                                 unidecode(instance.country.name)))
                 
                                                 
@receiver(pre_save, sender=Country)
def country_get_slug(sender, instance, **kwargs):
    instance.slug = slugify(unidecode(instance.name))                                               

