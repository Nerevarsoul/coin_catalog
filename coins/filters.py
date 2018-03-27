import rest_framework_filters as filters

from .models import Coin, Serie
 
__ALL__ = ('ListingSeriesFilter',)


class ListingSeriesFilter(filters.FilterSet):

    owner = filters.CharFilter(method='filter_by_owner')

    class Meta:
        model = Serie
        fields = ['name']

    def filter_by_owner(self, qs, name, value):
        if not value:
            return qs

        qs = qs.filter(
            id__in=Coin.objects.filter(owner=value).select_related('catalog_coin__serie').
                values_list('catalog_coin__serie__id', flat=True).distinct()
        )
        return qs
