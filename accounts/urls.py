from django.urls import include, path
from rest_framework.authtoken import views


urlpatterns = [
    path('', include('social_django.urls')),
    path('api-token-auth/', views.obtain_auth_token)
]
