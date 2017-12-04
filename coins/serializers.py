from rest_framework import serializers

from .models import CatalogCoin

__all__ = ('CatalogCoinListSerializer', 'CatalogCoinSerializer',)


class CatalogCoinListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogCoin
        fields = ('id', 'face_value', 'currency', 'year', 'theme', 'country', 'serie', 'mint', 'material',)


class CatalogCoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogCoin
        fields = '__all__'
