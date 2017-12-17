from django.urls import path

from .views import *


urlpatterns = [

    # catalogue
    path(
        'catalogue/',
        CatalogueCoinCreateListView.as_view(),
        name='catalogue'
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

