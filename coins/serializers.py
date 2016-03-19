from rest_framework import serializers

from .models import CatalogCoin

# Serializers define the API representation.
class CatalogCoinSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CatalogCoin
        fields = ('currency', 'face_value')
