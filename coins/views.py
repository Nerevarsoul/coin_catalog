from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from core.views import GetListOrCreateSerializerMixin

from .models import *
from .serializers import *

__all__ = ('CatalogueCoinCreateListView', 'CatalogueCoinDetailView', 'SerieCreateListView',)


class SerieCreateListView(GetListOrCreateSerializerMixin, ListCreateAPIView):
    queryset = Serie.objects.all()
    serializer_class = SerieListSerializer
    serializer_class_for_create = ''


class CatalogueCoinCreateListView(GetListOrCreateSerializerMixin, ListCreateAPIView):
    queryset = CatalogCoin.objects.list()
    serializer_class = CatalogCoinListSerializer
    serializer_class_for_create = CatalogCoinSerializer


class CatalogueCoinDetailView(RetrieveAPIView):
    queryset = CatalogCoin.objects.all()
    serializer_class = CatalogCoinSerializer

