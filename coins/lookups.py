# -*- coding: UTF-8  -*-
from __future__ import unicode_literals

from ajax_select import register, LookupChannel

from .models import CatalogCoins


@register('catalog_coin')
class CatalogLookup(LookupChannel):

    model = CatalogCoins

    def get_query(self, q, request):
        return self.model.objects.filter(name__icontains=q).order_by('name')
