# -*- coding: UTF-8  -*-
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.shortcuts import render_to_response
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView

from rest_framework import viewsets

from .forms import CatalogCoinsForm, CoinsForm
from .models import *
from .serializers import CatalogCoinSerializer


# Create your views here.
class IndexView(TemplateView):

    template_name = "index.html"


# CatalogCoins views
class CatalogCoinsTableView(ListView):

    model = CatalogCoin
    template_name = "coins.html"
    paginate_by = 20
    context_object_name = "coins"
    # queryset = CatalogCoin.objects.all()


class CatalogCoinsDetailView(DetailView):
    model = CatalogCoin
    template_name = "detail_view.html"
    context_object_name = "coin"


class CreateCatalogCoinsView(CreateView):

    model = Coin
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


# coins view
class CoinsUserView(ListView):
    
    model = Coin
    user = ""
    
    def get_context_data(self, **kwargs):
        context = super(CoinsUserView, self).get_context_data(**kwargs)
        context["user"] = self.get_user()
        return context
    
    def get_user(self):
        try:
            user = self.request.GET["user"]
        except KeyError:
            user = self.user
        return user
    
    def get_queryset(self):
        return self.model.objects.filter(country__exact=self.get_country)


class CoinsDetailView(DetailView):
    
    model = Coin
    form = CoinsForm


class CreateCoinsView(CreateView):
    
    model = Coin
    form = CoinsForm


class UpdateCoinsView(UpdateView):
    
    model = Coin


class CoinsCountryView(CatalogCoinsCountryView):
    
    model = Coin
    country = ""
    
    def get_context_data(self, **kwargs):
        context = super(CoinsCountryView, self).get_context_data(**kwargs)
        context["country"] = self.get_country()
        return context
    
    def get_country(self):
        try:
            country = self.request.GET["country"]
        except KeyError:
            country = self.country
        return country
    
    def get_queryset(self):
        return self.model.objects.filter(country__exact=self.get_country)


class CatalogCoinsViewSet(viewsets.ModelViewSet):

    queryset = CatalogCoin.objects.all()
    serializer_class = CatalogCoinSerializer