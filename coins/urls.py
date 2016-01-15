from django.conf.urls import include, url

from .views import IndexView, CatalogCoinsTableView, CreateCatalogCoinsView, UpdateUserView,\
    CatalogCoinsDetailView
from .vk import vkontakte_view


urlpatterns = [
    url(r'^index/$', IndexView.as_view(), name = 'index'),
    url(r'^catalogue/$', CatalogCoinsTableView.as_view(), name = 'catalogue'),
    url(r'^catalogue/(?P<country>\d+)/$', CatalogCoinsCountryiew.as_view(), name = 'catalogue_country'),
    url(r'^create_catalog_coins/$', CreateCoinsView.as_view(), name = 'create_catalog_coins'),
    url(r'^update_profile/$', UpdateUserView.as_view(), name = 'update_profile'),
    url(r'^catalog_coin_detail/(?P<slug>\d+)/$', CatalogCoinsDetailView.as_view(), 
        name = 'catalog_detail_coins'),
    url(r'^vk/', vkontakte_view, name='vk_app'),
    url(r'', include('social_auth.urls')),
]
