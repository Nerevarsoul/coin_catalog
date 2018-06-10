from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter()
router.register(r'series', SerieViewSet)
router.register(r'countries', CountryViewSet)


urlpatterns = [

    path(
        'catalogue/',
        CatalogueCoinCreateListView.as_view(),
        name='catalogue'
    ),
    path(
        'coins/',
        CoinCreateListView.as_view(),
        name='coins'
    ),
    path(
        'coin-by-series/',
        SerieCoinView.as_view(),
        name='coin-by-series'
    ),
    path(
        'catalogue/<slug:slug>/',
        CatalogueCoinDetailView.as_view(),
        name='catalogue_detail_coins'
    ),
    path(r'', include(router.urls))
]
