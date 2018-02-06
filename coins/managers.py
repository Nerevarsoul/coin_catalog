from django.db import models

__all__ = ('CatalogCoinManager', 'CoinManager')


class CatalogCoinQuerySet(models.QuerySet):

    def list(self):
        return self.select_related('serie').only(
            'id', 'face_value', 'currency', 'country', 'year', 'theme', 'mint', 'serie__name',
        )


class CatalogCoinManager(models.Manager):

    def get_queryset(self):
        return CatalogCoinQuerySet(self.model, using=self._db)

    def list(self):
        return self.get_queryset().list()


class CoinQuerySet(models.QuerySet):

    def list(self):
        return self.select_related('catalog_coin', 'catalog_coin__serie', 'owner').only(
            'id', 'catalog_coin__face_value', 'catalog_coin__currency', 'catalog_coin__country', 'catalog_coin__year',
            'catalog_coin__theme', 'catalog_coin__mint', 'catalog_coin__serie__name', 'owner__username',
        )


class CoinManager(models.Manager):

    def get_queryset(self):
        return CoinQuerySet(self.model, using=self._db)

    def list(self):
        return self.get_queryset().list()
