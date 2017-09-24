# -*- coding: UTF-8  -*-
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from .models import *
from .serializers import *

__all__ = ('CatalogueCoinCreateListView', 'CatalogueCoinDetailView',)


class CatalogueCoinCreateListView(ListCreateAPIView):
    queryset = CatalogCoin.objects.all()
    serializer_class = CatalogCoinListSerializer

    def get_serializer_class(self):
        if self.method == 'GET':
            return CatalogCoinListSerializer
        return CatalogCoinSerializer


class CatalogueCoinDetailView(RetrieveAPIView):
    queryset = CatalogCoin.objects.all()
    serializer_class = CatalogCoinSerializer
