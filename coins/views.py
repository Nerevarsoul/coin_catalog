from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from django_filters.rest_framework import DjangoFilterBackend

from core.views import GetListOrCreateSerializerMixin

from .filters import *
from .models import *
from .serializers import *

__all__ = ('CatalogueCoinCreateListView', 'CatalogueCoinDetailView', 'SerieCreateListView', 'CoinCreateListView',)


class SerieCreateListView(GetListOrCreateSerializerMixin, ListCreateAPIView):
    queryset = Serie.objects.all().only('name', 'level', 'tree_id')
    serializer_class = SerieListSerializer
    serializer_class_for_create = ''
    filter_class = ListingSerieFilter 


class CatalogueCoinCreateListView(GetListOrCreateSerializerMixin, ListCreateAPIView):
    queryset = CatalogCoin.objects.list()
    serializer_class = CatalogCoinListSerializer
    serializer_class_for_create = CatalogCoinSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('serie__name',)


class CatalogueCoinDetailView(RetrieveAPIView):
    queryset = CatalogCoin.objects.all()
    serializer_class = CatalogCoinSerializer


class CoinCreateListView(GetListOrCreateSerializerMixin, ListCreateAPIView):
    queryset = Coin.objects.list() 
    serializer_class = CoinListSerializer
    serializer_class_for_create = CoinSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('catalog_coin__serie__name', 'owner',)
