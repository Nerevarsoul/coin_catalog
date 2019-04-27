from django.contrib import admin

from .models import *


class SpiderJobAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'modified', 'result',)


class SpiderAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'url', 'created', 'modified', 'is_active', 'period', 'spider_name')


admin.site.register(SpiderJob, SpiderJobAdmin)
admin.site.register(Spider, SpiderAdmin)
