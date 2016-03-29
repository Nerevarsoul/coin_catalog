# -*- coding: UTF-8  -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView

from .forms import UserProfileForm
from .models import *


# Create your views here.
# users view
class UserListView(ListView):
    
    model = UserProfile
    template_name = "users.html"
    context_object_name = "profiles"
    
    def get_queryser(self):
        return self.model.objects.all().select_related('user', 'address')


class UserDetailView(DetailView):
    
    model = UserProfile


class UpdateUserView(UpdateView):

    model = UserProfile
    form_class = UserProfileForm
    success_url = reverse_lazy("index")
    template_name = "create_coin.html"
