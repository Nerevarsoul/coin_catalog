from django.db import models
from django.utils.translation import ugettext_lazy as _

from scheduler.models import BaseJob

from core.mixins import ErrorMixin


class SpiderJob(ErrorMixin, BaseJob):
    class Meta:
        verbose_name = _('Spider Job')
        verbose_name_plural = _('Spider Jobs')
        ordering = ('name',)

    result = models.PositiveIntegerField(default=0)
