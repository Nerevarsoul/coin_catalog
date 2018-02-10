import rest_framework_filters as filters

from .models import Coin, Serie
 
__ALL__ = ('ListingSerieFilter',)


def filter_owner(queryset, value):
    if not value:
        return queryset

    queryset = queryset.filter(
        id__in=Coin.objects.filter(owner=value).select_related('catalog_coin__serie').
            values_list('catalog_coin__serie__id', flat=True).distinct()
    )
    return queryset


class ListingSerieFilter(filters.FilterSet):

    owner = filters.CharFilter(action=filter_owner)

