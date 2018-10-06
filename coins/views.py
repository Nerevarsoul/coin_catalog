from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

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

    def create(self, request, *args, **kwargs):
        many = False
        if isinstance(request.data, list):
            many = True
            for coin in request.data:
                coin.update(owner=self.request.user.id)
        else:
            request.data.update(owner=self.request.user.id)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
