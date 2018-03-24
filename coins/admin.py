from django.contrib import admin

from dynamic_raw_id.admin import DynamicRawIDMixin
from mptt.admin import MPTTModelAdmin

from .models import *


@admin.register(Serie)
class SerieAdmin(MPTTModelAdmin):
    list_display = ('name', 'country', 'coin_amount', 'level', 'tree_id',)
    list_filter = ('country',)


@admin.register(CatalogCoin)
class CatalogCoinAdmin(DynamicRawIDMixin, admin.ModelAdmin):
    list_display = ('face_value', 'currency', 'year', 'serie', 'mint',)
    list_select_related = ('serie',)
    list_filter = (('serie', admin.RelatedOnlyFieldListFilter), 'year', 'country',)
    dynamic_raw_id_fields = ('serie',)  


@admin.register(Coin)
class CoinAdmin(DynamicRawIDMixin, admin.ModelAdmin):
    list_display = ('catalog_coin', 'get_serie', 'owner', 'get_year', 'status', 'get_mint',)
    list_select_related = ('catalog_coin', 'owner', 'catalog_coin__serie',)
    list_filter = (('catalog_coin__serie', admin.RelatedOnlyFieldListFilter), 'status',)
    ordering = ('catalog_coin__theme',)
    dynamic_raw_id_fields = ('catalog_coin',)

    def get_serie(self, instance):
        return instance.catalog_coin.serie.name

    def get_mint(self, instance):
        return instance.catalog_coin.mint

    def get_year(self, instance):
        return instance.catalog_coin.year

