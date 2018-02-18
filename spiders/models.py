from django.db import models
from django.utils.translation import ugettext_lazy as _

from scheduler.models import BaseJob
from model_utils.models import TimeStampedModel

from core.mixins import ErrorMixin


class SpiderJob(ErrorMixin, BaseJob):
    class Meta:
        verbose_name = _('Spider Job')
        verbose_name_plural = _('Spider Jobs')
        ordering = ('name',)

    result = models.PositiveIntegerField(default=0)


class Spider(TimeStampedModel):
    class Meta:
        verbose_name = _('Spider')
        verbose_name_plural = _('Spiders')
        ordering = ('created',)

    is_active = models.BooleanField(default=False)
    site_name = models.CharField(max_length=50)
    url = models.URLField()
    period = models.CharField(max_length=20)
    spider_name = models.CharField(max_length=50)
