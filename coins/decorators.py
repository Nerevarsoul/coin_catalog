# -*- coding: UTF-8  -*-
from __future__ import unicode_literals

from django.contrib.auth import BACKEND_SESSION_KEY
from django.contrib.auth.models import AnonymousUser
from django.core.cache import cache

from social_auth.backends.contrib.vk import VKOAuth2Backend
from social_auth.views import complete as social_complete


def is_complete_authentication(request):
    return request.user.is_authenticated() and \
           VKOAuth2Backend.__name__ in request.session.get(
            BACKEND_SESSION_KEY, ''
           )


def get_access_token(user):
    key = str(user.id)
    access_token = cache.get(key)

    # If cache is empty read the database
    if access_token is None:
        try:
            social_user = user.social_user if hasattr(user, 'social_user') \
                                           else UserSocialAuth.objects.get(
                                                user=user.id,
                                                provider=VKOAuth2Backend.name
                                           )
        except UserSocialAuth.DoesNotExist:
            return None

        if social_user.extra_data:
            access_token = social_user.extra_data.get('access_token')
            expires = social_user.extra_data.get('expires')

            cache.set(key, access_token, int(expires) if expires is not None
                                                      else 0)
    return access_token


# VK decorator to setup environment
def vkontakte_decorator(func):
    def wrapper(request, *args, **kwargs):
        user = request.user

        # User must me logged via VKontakte backend in order to ensure we talk
        # about the same person
        if not is_complete_authentication(request):
            try:
                user = social_complete(request, VKOAuth2Backend.name)
            except (ValueError, AttributeError):
                pass  # no matter if failed

        # Not recommended way for VK, but still something we need to be aware
        # of
        if isinstance(user, HttpResponse):
            kwargs.update({'auth_response': user})
        else:  # Need to re-check the completion
            if is_complete_authentication(request):
                kwargs.update({'access_token': get_access_token(request.user)})
            else:
                request.user = AnonymousUser()

        return func(request, *args, **kwargs)

    return wrapper