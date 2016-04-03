# -*- coding: UTF-8  -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView

from .forms import UserProfileForm
from .models import *


# Create your views here.
# users view
class UserListView(ListView):
    
    model = User
    template_name = "users.html"
    context_object_name = "profiles"
    
    def get_queryser(self):
        return self.model.objects.all().select_related('address')


class UserDetailView(DetailView):
    
    model = User


class UpdateUserView(UpdateView):

    model = User
    form_class = UserForm
    success_url = reverse_lazy("index")
    template_name = "create_coin.html"
