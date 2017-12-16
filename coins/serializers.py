from rest_framework import serializers

from .models import CatalogCoin, Serie

__all__ = ('CatalogCoinListSerializer', 'CatalogCoinSerializer', 'SerieListSerializer',)


class SerieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = ('id', 'name')


class CatalogCoinListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogCoin
        fields = ('id', 'face_value', 'currency', 'country', 'year', 'theme', 'mint', 'serie',)

        serie = serializers.SlugRelatedField(slug_field='name', read_only=True)


class CatalogCoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogCoin
        fields = '__all__'

