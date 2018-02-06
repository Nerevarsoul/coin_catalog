from django.urls import path

from .views import *


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
        'catalogue/<slug:slug>/',
        CatalogueCoinDetailView.as_view(),
        name='catalogue_detail_coins'
    ),
    path(
        'series/',
        SerieCreateListView.as_view(),
        name='serie_list'
    ),
]
