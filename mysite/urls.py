from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'', include('core.urls')),
    url(r'api/', include('coins.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
