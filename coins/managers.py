from django.db import models


class CatalogCoinQuerySet(models.QuerySet):

    def list(self):
        return self.select_related('serie').only('id', 'face_value', 'currency', 'country', 'year', 'theme', 'mint', 'serie__name')


class CatalogCoinManager(models.Manager):

    def get_queryset(self):
        return CatalogCoinQuerySet(self.model, using=self._db)

    def list(self):
        return self.get_queryset().list()

