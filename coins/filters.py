# -*- coding: UTF-8  -*-
import django_filters

from .models import Coin


class CoinsFilter(django_filters.FilterSet):

    class Meta:
        model = Coin
        fields = {
            "catalog_coin": ["contain"],
            "condition": ["exact"]
        }
