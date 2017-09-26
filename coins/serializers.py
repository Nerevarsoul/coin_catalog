from rest_framework import serializers

from .models import CatalogCoin

__all__ = ('CatalogCoinListSerializer', 'CatalogCoinSerializer',)


class CatalogCoinListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogCoin
        fields = (
            'face_value',
            'currency',
            'country',
            'circulation',
            'slug',
        )


class CatalogCoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogCoin
        fields = '__all__'
