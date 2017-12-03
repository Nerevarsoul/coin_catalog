from django.urls import include, path
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    # path(r'', include('core.urls')),
    path('api/', include('coins.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
