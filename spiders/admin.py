from django.contrib import admin

from .models import *


class SpiderJobAdmin(admin.ModelAdmin):
    list_display = ('name', 'scheduled_time', 'created', 'modified', 'result',)

admin.site.register(SpiderJob, SpiderJobAdmin)
