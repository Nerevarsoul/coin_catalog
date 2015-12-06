# -*- coding: UTF-8  -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from django_tables2 import SingleTableView

from .forms import *
from .decorators import vkontakte_decorator
from .models import *
from .tables import *


# Create your views here.
class IndexView(TemplateView):

	template_name = "index.html"


@vkontakte_decorator
def vkontakte_view(request, *args, **kwargs):
    # If there is a ready response just return it. Not recommended because
    # pipeline redirects fail the normal workflow here.
    auth_response = kwargs.get('auth_response')
    if auth_response:
        for item in auth_response.items():
            if item[0] == 'Location' and 'form' in item[1]:
                return auth_response

    return render_to_response('vkontakte_app.html', {
        'vk_app_id': settings.VKONTAKTE_APP_AUTH['id']
                        if hasattr(settings, 'VKONTAKTE_APP_AUTH') else None,
        'app_scope': ','.join(settings.VKONTAKTE_OAUTH2_EXTRA_SCOPE),
        'warning': not request.GET.get('user_id')
    }, RequestContext(request))


class CoinsTableView(SingleTableView):

    model = Coins
    table_class = CoinsTable
    template_name = "coins.html"


class CreateCoinsView(CreateView):

	model = Coins
	form_class = CoinsForm
	success_url = reverse_lazy("coins")
	template_name = "create_coin.html"
