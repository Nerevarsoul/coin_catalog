from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter()
router.register(r'series', SerieViewSet)


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
    path(r'', include(router.urls))
]
