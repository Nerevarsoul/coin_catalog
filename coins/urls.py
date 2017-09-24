# -*- coding: UTF-8  -*-
from django.conf.urls import include, url

from .views import *


urlpatterns = [

    # catalogue
    url(r'^catalogue/$', CatalogueCoinCreateListView.as_view(), name='catalogue'),
    url(r'^catalogue/(?P<slug>\d+)/$', CatalogueCoinDetailView.as_view(),
        name='catalogue_detail_coins'),

]
