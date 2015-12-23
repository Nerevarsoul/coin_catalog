# -*- coding: UTF-8  -*-
from __future__ import unicode_literals

import django_filters

from .models import Coins


class CoinsFilter(django_filters.FilterSet):
    class Meta:
        model: Coins
        fields = {
            "catalog_coin": ["contain"]
            "condition": ["exact"]
        }
