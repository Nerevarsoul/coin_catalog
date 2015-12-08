from django.conf.urls import include, url

from .views import IndexView, CoinsTableView, CreateCoinsView, UpdateUserView
from .vk import vkontakte_view


urlpatterns = [
    url(r'^index/$', IndexView.as_view(), name = 'index'),
    url(r'^coins/$', CoinsTableView.as_view(), name = 'coins'),
    url(r'^create_coins/$', CreateCoinsView.as_view(), name = 'create_coins'),
    url(r'^update_profile/$', UpdateUserView.as_view(), name = 'create_coins'),
    url(r'^vk/', vkontakte_view, name='vk_app'),
    url(r'', include('social_auth.urls')),
]