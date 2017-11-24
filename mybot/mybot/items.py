# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from scrapy_djangoitem import DjangoItem

from coins.models import CatalogCoin, Serie


class CoinItem(DjangoItem):
    django_model = CatalogCoin


class SerieItem(DjangoItem):
    django_model = Serie

