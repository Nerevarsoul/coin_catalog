# -*- coding: UTF-8  -*-
from __future__ import unicode_literals

from django.conf.urls import include, url

from .views import UpdateUserView, UserListView
# from .vk import vkontakte_view


urlpatterns = [
    # user 
    url(r'^users_list/$', UserListView.as_view(), name='users_list'),  
    url(r'^update_profile/$', UpdateUserView.as_view(), name='update_profile'),
    
    # (r'^vk/', vkontakte_view, name='vk_app'),
    # url(r'', include('social_auth.urls')),
]
