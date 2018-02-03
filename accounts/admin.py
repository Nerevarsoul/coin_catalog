from django.contrib import admin
# from django.contrib.auth.models import User as DjangoUser

from .models import *


class UserAdmin(admin.ModelAdmin):
    pass

# admin.site.unregister(DjangoUser)
admin.site.register(User, UserAdmin)
