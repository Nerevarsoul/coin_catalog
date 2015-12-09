from django.contrib import admin

from .models import *


# Register your models here.
admin.site.register(Coins)
admin.site.register(CatalogCoins)
admin.site.register(Country)
admin.site.register(Address)
admin.site.register(UserProfile)