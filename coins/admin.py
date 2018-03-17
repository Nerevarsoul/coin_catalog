from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from .models import *


class SerieAdmin(MPTTModelAdmin):
    list_display = ('name', 'country', 'coin_amount', 'level', 'tree_id',)


class CatalogCoinAdmin(admin.ModelAdmin):
    list_display = ('face_value', 'currency', 'year', 'serie', 'mint',)
    list_select_related = ('serie',)
    list_filter = (('serie', admin.RelatedOnlyFieldListFilter), 'year')  


class CoinAdmin(admin.ModelAdmin):
    list_display = ('catalog_coin', 'get_serie', 'owner', 'get_year', 'status', 'get_mint',)
    list_select_related = ('catalog_coin', 'owner', 'catalog_coin__serie',)
    list_filter = (('catalog_coin__serie', admin.RelatedOnlyFieldListFilter), 'status',)
    ordering = ('catalog_coin__theme',)

    def get_serie(self, instance):
        return instance.catalog_coin.serie.name

    def get_mint(self, instance):
        return instance.catalog_coin.mint

    def get_year(self, instance):
        return instance.catalog_coin.year


# Register your models here.
admin.site.register(Serie, SerieAdmin)
admin.site.register(CatalogCoin, CatalogCoinAdmin)
admin.site.register(Coin, CoinAdmin)
