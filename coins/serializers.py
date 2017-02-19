from rest_framework import serializers

from .models import CatalogCoin


class CatalogCoinPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogCoin
        fields = [
            'id',
            'face_value',
            'currency',
            'slug',
        ]


class CatalogCoinDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogCoin
        fields = [
            'face_value',
            'currency',
]
