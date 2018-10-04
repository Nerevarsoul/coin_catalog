from django.db.models import QuerySet, Manager, Count, Q

__all__ = ('CatalogCoinManager', 'CoinManager', 'SeriesManager',)


class CatalogCoinQuerySet(QuerySet):

    def list(self):
        return self.select_related('serie').only(
            'id', 'face_value', 'currency', 'country', 'year', 'theme', 'mint', 'serie__name',
        )

    def list_with_coins(self, user):
        return self.list().prefetch_related('coins').annotate(
            collection=Count('coins', filter=Q(coins__status='in_collection', coins__owner=user)),
            exchange=Count('coins', filter=Q(coins__status='for_exchange', coins__owner=user)),
            wishlist=Count('coins', filter=Q(coins__status='in_wishlist', coins__owner=user))
        )

    def series_list(self, serie):
        return self.select_related('serie').filter(serie=serie).only(
            'id', 'face_value', 'currency', 'country', 'year', 'theme', 'mint', 'serie__name',
        ).distinct('crause_number')


class CatalogCoinManager(Manager):

    def get_queryset(self):
        return CatalogCoinQuerySet(self.model, using=self._db)

    def list(self):
        return self.get_queryset().list()

    def list_with_coins(self, user):
        return self.get_queryset().list_with_coins(user)

    def series_list(self, serie):
        return self.get_queryset().series_list(serie)


class CoinQuerySet(QuerySet):

    def list(self):
        return self.select_related('catalog_coin', 'catalog_coin__serie', 'owner').only(
            'id', 'catalog_coin__face_value', 'catalog_coin__currency', 'catalog_coin__country', 'catalog_coin__year',
            'catalog_coin__theme', 'catalog_coin__mint', 'catalog_coin__serie__name', 'owner__username',
        )


class CoinManager(Manager):

    def get_queryset(self):
        return CoinQuerySet(self.model, using=self._db)

    def list(self):
        return self.get_queryset().list()


class SeriesQuerySet(QuerySet):

    def list(self):
        return self.only('name', 'level', 'tree_id', 'is_active',)


class SeriesManager(Manager):

    def get_queryset(self):
        return SeriesQuerySet(self.model, using=self._db)

    def list(self):
        return self.get_queryset().list()
