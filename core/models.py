# -*- coding: UTF-8  -*-
from datetime import datetime

from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import signals


COUNTRY_STATUS = (
    (1, 'Не существующая'),
    (2, 'Существующая'),
)


class AppQuerySet(models.QuerySet):

    def delete(self, **kwargs):
        return self.update(is_void=True)


class AppManager(models.Manager):
    queryset_class = AppQuerySet
    use_for_related_fields = True

    def get_queryset(self, exclude_void=True):
        q = self.queryset_class(self.model)
        if hasattr(self, 'core_filters'):
            q = q.filter(
                **self.core_filters
            )

        if exclude_void:
            q = q.exclude(is_void=True)
        return q

    def all_objects_including_void(self):
        return self.get_queryset(exclude_void=False)
        
        
class AppModel(models.Model):
    is_void = models.BooleanField(default=False)
    date_of_delete = models.DatetimeField()
    objects = AppManager()

    class Meta:
        abstract = True

    def delete(self, **kwargs):
        self.is_void = True
        self.date_of_delete = datetime.now()
        self.save()
        signals.post_delete.send(
            sender=self.__class__, instance=self
        )


class Image(models.Model):

    image = models.ImageField(upload_to='coin_images',)


class Country(models.Model):

    name = models.CharField(max_length=50)
    status = models.IntegerField(choices=COUNTRY_STATUS)
    slug = models.SlugField(max_length=55)

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('country_view', args=[self.slug])
