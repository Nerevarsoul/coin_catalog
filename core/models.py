# -*- coding: UTF-8  -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models


COUNTRY_STATUS = (
    (1, 'Не существующая'),
    (2, 'Существующая'),
)


# Create your models here.
class Image(models.Model):

    image = models.ImageField(upload_to='coin_images',)


class Country(models.Model):

    name = models.CharField(max_length=50)
    status = models.IntegerField(choices=COUNTRY_STATUS)
    slug = models.SlugField(max_length=55)

    def __unicode__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('country_view', args=[self.slug])
