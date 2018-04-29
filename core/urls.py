from django.urls import path, re_path
from .views import IndexView


urlpatterns = [
    path('', IndexView.as_view()),
    re_path('^coins.*', IndexView.as_view()),
    re_path('^catalogue.*', IndexView.as_view()),
]
