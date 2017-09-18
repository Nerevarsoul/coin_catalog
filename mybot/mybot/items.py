# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from scrapy_djangoitem import DjangoItem

from coins.models import CatalogCoin


class EuroCoinsItem(DjangoItem):
    django_model = CatalogCoin
