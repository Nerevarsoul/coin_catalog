from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.postgres.fields import JSONField

from prettyjson import PrettyJSONWidget

from .models import *


@admin.register(User)
class UserAdmin(UserAdmin):
    formfield_overrides = {
        JSONField: {'widget': PrettyJSONWidget(attrs={'initial': 'parsed'})}
    }
