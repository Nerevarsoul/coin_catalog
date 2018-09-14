from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from core.views import GetListOrCreateSerializerMixin
from .filters import *
from .models import *
from .serializers import *

__all__ = (
    'CatalogueCoinCreateListView', 'CatalogueCoinDetailView', 'SerieViewSet', 'CoinCreateListView', 'CountryViewSet',
    'SerieCoinView',
)


class CountryViewSet(ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountriesListSerializer


class SerieViewSet(ReadOnlyModelViewSet):
    queryset = Serie.objects.list()
    serializer_class = SeriesListSerializer
    filter_class = ListingSeriesFilter


class CatalogueCoinCreateListView(GetListOrCreateSerializerMixin, ListCreateAPIView):
    queryset = CatalogCoin.objects.all()
    serializer_class = CatalogCoinListSerializer
    serializer_class_for_create = CatalogCoinSerializer
    pagination_class = PageNumberPagination
    filter_fields = ('serie__name',)

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if not user.is_anonymous:
            return qs.list_with_coins(self.request.user)
        return qs.list()
    

class CatalogueCoinDetailView(RetrieveAPIView):
    queryset = CatalogCoin.objects.all()
    serializer_class = CatalogCoinSerializer


class SerieCoinView(ListAPIView):
    queryset = CatalogCoin.objects.all()
    serializer_class = CatalogCoinListSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.serie('country')


class CoinCreateListView(GetListOrCreateSerializerMixin, ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Coin.objects.list() 
    serializer_class = CoinListSerializer
    serializer_class_for_create = CoinSerializer
    filter_fields = ('catalog_coin__serie__name', 'owner', 'status',)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
