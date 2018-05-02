from rest_framework import serializers

from .models import *

__all__ = (
    'CatalogCoinListSerializer', 'CatalogCoinSerializer', 'SeriesListSerializer', 'CoinListSerializer',
    'CoinSerializer', 'CountriesListSerializer',
)


class CountriesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name', 'flag',)


class SeriesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = ('name',)


class CatalogCoinListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogCoin
        fields = (
            'id', 'face_value', 'currency', 'country', 'year', 'theme', 'mint', 'serie', 'collection', 'exchange',
            'wishlist',
        )

    serie = serializers.SlugRelatedField(slug_field='name', read_only=True)
    collection = serializers.IntegerField(read_only=True)
    exchange = serializers.IntegerField(read_only=True)
    wishlist = serializers.IntegerField(read_only=True)


class CatalogCoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogCoin
        fields = '__all__'


class CoinListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = ('id', 'catalog_coin', 'owner', 'status',)

    catalog_coin = CatalogCoinListSerializer()


class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = '__all__'
