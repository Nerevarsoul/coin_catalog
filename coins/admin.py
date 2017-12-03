from django.contrib import admin


from .models import *


class CatalogCoinAdmin(admin.ModelAdmin):
    list_display = ('face_value', 'currency', 'year', 'theme', 'serie',)


# Register your models here.
admin.site.register(Serie)
admin.site.register(CatalogCoin, CatalogCoinAdmin)
admin.site.register(Coin)

