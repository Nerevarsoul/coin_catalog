from django.contrib import admin
from django.contrib.postgres.fields import JSONField

from dynamic_raw_id.admin import DynamicRawIDMixin
from import_export.admin import ImportMixin
from mptt.admin import MPTTModelAdmin
from prettyjson import PrettyJSONWidget

from .models import *
from .resources import CatalogCoinResource


@admin.register(Serie)
class SerieAdmin(MPTTModelAdmin):
    list_display = ('name', 'country', 'coin_amount', 'level', 'tree_id',)
    list_filter = ('country',)


@admin.register(CatalogCoin)
class CatalogCoinAdmin(DynamicRawIDMixin, ImportMixin, admin.ModelAdmin):
    list_display = ('face_value', 'currency', 'year', 'country', 'serie', 'theme', 'mint',)
    list_select_related = ('serie',)
    list_filter = (('serie', admin.RelatedOnlyFieldListFilter), 'country', 'year', 'face_value',)
    dynamic_raw_id_fields = ('serie',)
    resource_class = CatalogCoinResource


@admin.register(Coin)
class CoinAdmin(DynamicRawIDMixin, admin.ModelAdmin):
    formfield_overrides = {
        JSONField: {'widget': PrettyJSONWidget(attrs={'initial': 'parsed'})}
    }
    list_display = ('catalog_coin', 'get_serie', 'get_country', 'owner', 'get_year', 'status', 'get_mint',)
    list_select_related = ('catalog_coin', 'owner', 'catalog_coin__serie',)
    list_filter = (
        ('catalog_coin__serie', admin.RelatedOnlyFieldListFilter), 
        'status', 'catalog_coin__country', 'catalog_coin__year',
        'catalog_coin__face_value', 'catalog_coin__currency',
    )
    ordering = ('catalog_coin__theme',)
    dynamic_raw_id_fields = ('catalog_coin',)

    @staticmethod
    def get_serie(instance):
        return instance.catalog_coin.serie.name

    @staticmethod
    def get_mint(instance):
        return instance.catalog_coin.mint

    @staticmethod
    def get_year(instance):
        return instance.catalog_coin.year

    @staticmethod
    def get_country(instance):
        return instance.catalog_coin.country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass
