from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import *


class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Information'


class UserAdmin(UserAdmin):
    inlines = (UserInline,)


# Register your models here.
admin.site.register(Coins)
admin.site.register(CatalogCoins)
admin.site.register(Country)
admin.site.register(Address)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)