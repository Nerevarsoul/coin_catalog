# -*- coding: UTF-8  -*-
from __future__ import unicode_literals

from django.conf.urls import include, url

from rest_framework import routers

from .views import IndexView, CatalogCoinsTableView, CreateCatalogCoinsView, UpdateUserView, UserListView, \
    CatalogCoinsDetailView, CatalogCoinsCountryView, CoinsCountryView, CreateCoinsView, CoinsDetailView, CatalogCoinsViewSet
# from .vk import vkontakte_view


router = routers.DefaultRouter()
router.register(r'catalog_coins', CatalogCoinsViewSet)


urlpatterns = [
    url(r'^index/$', IndexView.as_view(), name='index'),
    
    # catalogue
    url(r'^catalogue/$', CatalogCoinsTableView.as_view(), name='catalogue'),
    url(r'^catalogue/(?P<country>\d+)/$', CatalogCoinsCountryView.as_view(),
        name='catalogue_country'),
    url(r'^create_catalog_coins/$', CreateCatalogCoinsView.as_view(),
        name='create_catalog_coins'),
    url(r'^catalog_coin_detail/(?P<slug>\d+)/$', CatalogCoinsDetailView.as_view(), 
        name='catalog_detail_coins'),
    
    # user 
    url(r'^users_list/$', UserListView.as_view(), name='users_list'),  
    url(r'^update_profile/$', UpdateUserView.as_view(), name='update_profile'),
    
    # coins
    # url(r'^coins/$', CoinsTableView.as_view(), name='catalogue'),
    url(r'^coins/(?P<country>\d+)/$', CoinsCountryView.as_view(),
        name='coins_country'),
    url(r'^create_coins/$', CreateCoinsView.as_view(),
        name='create_coins'),
    url(r'^coin_detail/(?P<slug>\d+)/$', CoinsDetailView.as_view(), 
        name='detail_coins'),
    
    # (r'^vk/', vkontakte_view, name='vk_app'),
    # url(r'', include('social_auth.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
