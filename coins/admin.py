from django.contrib import admin


from .models import *


class CatalogCoinAdmin(admin.ModelAdmin):
    list_display = ('face_value', 'currency', 'year', 'theme', 'serie',)
    list_select_related = ('serie',)  


class CoinAdmin(admin.ModelAdmin):
    list_display = ('catalog_coin', 'get_theme', 'get_serie', 'owner', 'status',)
    list_select_related = ('catalog_coin', 'owner', 'catalog_coin__serie',)
    list_filter = (('catalog_coin__serie', admin.RelatedOnlyFieldListFilter), 'status',)

    def get_theme(self, instance):
        return instance.catalog_coin.theme

    def get_serie(self, instance):
        return instance.catalog_coin.serie.name


# Register your models here.
admin.site.register(Serie)
admin.site.register(CatalogCoin, CatalogCoinAdmin)
admin.site.register(Coin, CoinAdmin)

