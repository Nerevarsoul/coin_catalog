 # -*- coding: UTF-8  -*-
from __future__ import unicode_literals

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

from .models import CatalogCoins


@receiver(pre_save, sender=CatalogCoins)
def catalog_get_slug(sender, instance, **kwargs):
    instance.slug = slugify("{} {} {} {}".format(instance.face_value, 
                                                 instance.currency, 
                                                 instance.circulation, 
                                                 instance.country))
                                                 
