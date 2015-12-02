from django.conf.urls import include, url

from .views import IndexView, CoinsTableView


urlpatterns = [
    url(r'^index/$', IndexView.as_view(), name = 'index'),
    url(r'^coins/$', CoinsTableView.as_view(), name = 'coins'),
]