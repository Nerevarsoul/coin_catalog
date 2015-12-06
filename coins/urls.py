from django.conf.urls import include, url

from .views import IndexView, CoinsTableView, CreateCoinsView


urlpatterns = [
    url(r'^index/$', IndexView.as_view(), name = 'index'),
    url(r'^coins/$', CoinsTableView.as_view(), name = 'coins'),
    url(r'^create_coins/$', CreateCoinsView.as_view(), name = 'create_coins'),
    url(r'^vk/', "coins.views.vkontakte_view", name='vk_app'),
]