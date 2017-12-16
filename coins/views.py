from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from core.views import RelatedMixin, GetListOrCreateSerializerMixin

from .models import *
from .serializers import *

__all__ = ('CatalogueCoinCreateListView', 'CatalogueCoinDetailView', 'SerieCreateListView',)


class SerieCreateListView(GetListOrCreateSerializerMixin, ListCreateAPIView):
    queryset = Serie.objects.all()
    serializer_class = SerieListSerializer
    serializer_class_for_create = ''


class CatalogueCoinCreateListView(RelatedMixin, GetListOrCreateSerializerMixin, ListCreateAPIView):
    queryset = CatalogCoin.objects.all()
    serializer_class = CatalogCoinListSerializer
    serializer_class_for_create = CatalogCoinSerializer
    list_select_related = ('serie',)


class CatalogueCoinDetailView(RetrieveAPIView):
    queryset = CatalogCoin.objects.all()
    serializer_class = CatalogCoinSerializer

