# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from scrapy.contrib.djangoitem import DjangoItem

from coins.models import CatalogCoin


# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

class EuroCoinsItem(DjangoItem):

    django_model = CatalogCoin
