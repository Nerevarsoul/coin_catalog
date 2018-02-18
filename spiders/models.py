from django.db import models

from django.utils.translation import ugettext_lazy as _

from django-rq-scheduler import BaseJob
from model_utils.models import TimeStampedModel

from core.mixins import ErrorMixin


class SpiderJob(ErrorMixin, TimeStampedModel, BaseJob):
    class Meta:
        verbose_name = _('Spider Job')
        verbose_name_plural = _('Spider Jobs')
        ordering = ('name',)

    result = models.PositiveIntegerField(default=0)
