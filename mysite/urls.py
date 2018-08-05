from django.urls import include, path
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/dynamic_raw_id/', include('dynamic_raw_id.urls')),
    path('api/auth/', include('accounts.urls')),
    path('django-rq/', include('django_rq.urls')),
    path('api/', include('coins.urls')),
    path('', include('core.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
