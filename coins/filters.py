import rest_framework_filters as filters
from django.db.models import Q

from .models import Coin, Serie, Country
 
__ALL__ = ('ListingSeriesFilter',)


class ListingSeriesFilter(filters.FilterSet):

    owner = filters.CharFilter(method='filter_by_owner')
    country = filters.CharFilter(method='filter_by_country')

    class Meta:
        model = Serie
        fields = ('name',)

    def filter_by_owner(self, qs, name, value):
        if not value:
            return qs

        qs = qs.filter(
            id__in=Coin.objects.filter(owner=value).select_related('catalog_coin__serie').
                values_list('catalog_coin__serie__id', flat=True).distinct()
        )
        return qs

    def filter_by_country(self, qs, name, value):
        if not value:
            return qs

        qs = qs.filter(
            Q(name=value) |
            Q(id__in=Country.objects.filter(parent=value).values_list('id', flat=True).distinct())
        )
        return qs
