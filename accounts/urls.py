# -*- coding: UTF-8  -*-
from django.conf.urls import include, url

import views

# from .vk import vkontakte_view


urlpatterns = [
    # user
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.logout, name='logout'),

    url(r'^users_list/$', views.UserListView.as_view(), name='users_list'),
    url(r'^update_profile/$', views.UpdateUserView.as_view(), name='update_profile'),
    
    # (r'^vk/', vkontakte_view, name='vk_app'),
    # url(r'', include('social_auth.urls')),
]
