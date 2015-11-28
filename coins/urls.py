from django.conf.urls import include, url

from .views import IndexView


urlpatterns = [
    url(r'index/$', IndexView.as_view(), name = 'index'),
]