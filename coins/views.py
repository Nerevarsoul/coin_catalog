# -*- coding: UTF-8  -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from django_tables2 import SingleTableView

from .forms import *
from .models import *
from .tables import *


# Create your views here.
class IndexView(TemplateView):

	template_name = "index.html"


class CoinsTableView(SingleTableView):

    model = Coins
    table_class = CoinsTable
    template_name = "coins.html"


class CreateCoinsView(CreateView):

	model = Coins
	form_class = CoinsForm
	success_url = reverse_lazy("coins")
	template_name = "create_coin.html"
