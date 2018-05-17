from django.contrib import admin
from django.contrib.postgres.fields import JSONField

from prettyjson import PrettyJSONWidget

from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField: {'widget': PrettyJSONWidget(attrs={'initial': 'parsed'})}
    }
