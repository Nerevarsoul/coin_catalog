from rest_framework import serializers

from .models import Coin, CatalogCoin, Serie

__all__ = (
    'CatalogCoinListSerializer', 'CatalogCoinSerializer', 'SerieListSerializer', 'CoinListSerializer',
    'CoinSerializer',
)


class SerieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = ('name',)


class CatalogCoinListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogCoin
        fields = ('id', 'face_value', 'currency', 'country', 'year', 'theme', 'mint', 'serie',)

    serie = serializers.SlugRelatedField(slug_field='name', read_only=True)


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
