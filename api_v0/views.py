from rest_framework import viewsets
from coins.serializers import *


class CatalogCoinViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CatalogCoin.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CatalogCoinPreviewSerializer
        return CatalogCoinDetailSerializer
