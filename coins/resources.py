from import_export import resources

from .models import CatalogCoin

__all__ = ('CatalogCoinResource',)


class CatalogCoinResource(resources.ModelResource):

    class Meta:
        model = CatalogCoin
        exclude = ('id', 'catalog_image', 'created', 'modified',)
