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

    def post(self, request, *args, **kwargs):
        request.data.update(owner=self.request.user.id)
        return super().create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        count = request.data.pop('count', None)
        if count:
            count = self.get_count(count, request.data['catalog_coin'], request.data['status'])
            if count:
                serializer = self.get_multiple_data(request, count)
            else:
                return Response({'error': 1}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_count(self, count, catalog_coin, coin_status):
        db_count = Coin.objects.filter(
            owner=self.request.user.id, catalog_coin=catalog_coin, status=coin_status
        ).count()
        return count - db_count if count - db_count > 0 else 0

    def get_multiple_data(self, request, count):
        if count > 1:
            data = [request.data] * count
            return self.get_serializer(data=data, many=True)
        else:
            return self.get_serializer(data=request.data)
