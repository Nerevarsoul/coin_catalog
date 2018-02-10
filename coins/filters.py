from django_filters import rest_framework as filters

from .models import Coin


class ListingSerieFilter(filters.FilterSet):

    serie = filters.CharFilter(action=filter_serie)    

    def filter_serie(queryset, value):
        if not value:
            return queryset

        queryset = queryset.filter(
            id__in=Coin.objects.filter(owner=value).select_related('catalog_coin__serie').
                values_list('catalog_coin__serie__id', flat=True).distinct()
        )
        return queryset

