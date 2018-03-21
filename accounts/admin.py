from django.contrib import admin
from rest_framework.authtoken.models import Token

from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    pass
