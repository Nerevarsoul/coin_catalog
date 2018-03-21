import logging

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from requests.exceptions import HTTPError
from social_core.exceptions import AuthException
from social_core.utils import get_strategy, parse_qs, user_is_authenticated
from social_django.utils import psa, STORAGE

from .serializers import UserTokenSerializer, OAuth2InputSerializer

l = logging.getLogger(__name__)


REDIRECT_URI = getattr(settings, 'REST_SOCIAL_OAUTH_REDIRECT_URI', '/')
DOMAIN_FROM_ORIGIN = getattr(settings, 'REST_SOCIAL_DOMAIN_FROM_ORIGIN', True)
LOG_AUTH_EXCEPTIONS = getattr(settings, 'REST_SOCIAL_LOG_AUTH_EXCEPTIONS', True)


def load_strategy(request=None):
    return get_strategy('rest_social_auth.strategy.DRFStrategy', STORAGE, request)


@psa(REDIRECT_URI, load_strategy=load_strategy)
def decorate_request(request, backend):
    pass


class BaseSocialAuthView(GenericAPIView):
    serializer_class = UserTokenSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny,)
    oauth2_serializer_class_in = OAuth2InputSerializer

    def get_serializer_in_data(self):
        """
        Compile the incoming data into a form fit for the serializer_in class.
        :return: Data for serializer in the form of a dictionary with 'provider' and 'code' keys.

        """
        return self.request.data.copy()

    def get_serializer_in(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = self.get_serializer_class_in()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    @method_decorator(never_cache)
    def post(self, request, *args, **kwargs):
        input_data = self.get_serializer_in_data()
        provider_name = self.get_provider_name(input_data)
        if not provider_name:
            return self.respond_error("Provider is not specified")
        self.set_input_data(request, input_data)
        decorate_request(request, provider_name)
        serializer_in = self.get_serializer_in(data=input_data)
        serializer_in.is_valid(raise_exception=True)
        try:
            user = self.get_object()
        except (AuthException, HTTPError) as e:
            return self.respond_error(e)
        if isinstance(user, HttpResponse):  # An error happened and pipeline returned HttpResponse instead of user
            return user
        resp_data = self.get_serializer(instance=user)
        self.do_login(request.backend, user)
        return Response(resp_data.data)

    def get_provider_name(self, input_data):
        if 'provider' in input_data:
            return input_data['provider']
        else:
            return self.kwargs.get('provider')

    def respond_error(self, error):
        if isinstance(error, Exception):
            if not isinstance(error, AuthException) or LOG_AUTH_EXCEPTIONS:
                self.log_exception(error)
        else:
            l.error(error)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def set_input_data(self, request, auth_data):
        """
        auth_data will be used used as request_data in strategy
        """
        request.auth_data = auth_data
