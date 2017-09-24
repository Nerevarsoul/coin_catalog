from rest_framework import serializers

from .models import CatalogCoin

__all__ = ('CatalogCoinListSerializer', 'CatalogCoinSerializer',)


class CatalogCoinListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogCoin
        fields = [
            'id',
            'face_value',
            'currency',
            'slug',
        ]


class CatalogCoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogCoin
        fields = [
            'face_value',
            'currency',
]
