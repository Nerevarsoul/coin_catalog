# -*- coding: UTF-8  -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from django_tables2 import SingleTableView

from .forms import UserProfileForm, CatalogCoinsForm
from .models import *
from .tables import *


# Create your views here.
class IndexView(TemplateView):

    template_name = "index.html"


# CatalogCoins views
class CatalogCoinsTableView(SingleTableView):

    model = CatalogCoins
    table_class = CoinsTable
    template_name = "coins.html"
    table_pagination = 20


class CatalogCoinsDetailView(DetailView):
    model = CatalogCoins
    template_name = "detail_view.html"
    context_object_name = "coin"


class CreateCatalogCoinsView(CreateView):

    model = Coins
    form_class = CatalogCoinsForm
    success_url = reverse_lazy("coins")
    template_name = "create_coin.html"
    
    
class CatalogCoinsCountryView(CatalogCoinsTableView):

    def get_queryset(self):

        return super(CatalogCoinsTableView, self).get_queryset().\
            filter(country__exact=Country.objects.get(slug__exact=self.kwargs['country']))
            
            
class CountryListView(ListView):
    
    model = Country
            
            
class CountryCreateView(CreateView):
    
    model = Country
    success_url = reverse_lazy("country_list")


# users view
class UserListView(ListView):
    pass


class UserDetailView(DetailView):
    pass


class UpdateUserView(UpdateView):

    model = UserProfile
    form_class = UserProfileForm
    success_url = reverse_lazy("index")
    template_name = "create_coin.html"


# coins view
class CoinsUserView(SingleTableView):
    
    model = Coins


class CoinsDetailView(DetailView):
    
    model = Coins


class CreateCoinsView(CreateView):
    
    model = Coins


class UpdateCoinsView(UpdateView):
    
    model = Coins


class CoinsCountryView(CatalogCoinsCountryView):
    
    model = Coins
