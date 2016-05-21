# -*- coding: UTF-8  -*-
from unidecode import unidecode

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

from .models import CatalogCoin


@receiver(pre_save, sender=CatalogCoin)
def catalog_get_slug(sender, instance, **kwargs):
    instance.slug = slugify("{} {} {} {}".format(instance.face_value, 
                                                 unidecode(instance.currency), 
                                                 instance.circulation, 
                                                 unidecode(instance.country.name)))
