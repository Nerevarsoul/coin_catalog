# -*- coding: UTF-8  -*-
from django.contrib import auth
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView

from .forms import LoginForm, UserForm
from .models import *


# users view
def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            if 'picture' in request.FILES:
                user.avatar = request.FILES['avatar']
            user.save()
            registered = True
            return redirect('index')
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render_to_response('accounts/register.html',
                              {'form': user_form,
                               'registered': registered}, context)


def login(request):
    context = RequestContext(request)
    login_form = LoginForm()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('view_profile', user.id)
        else:
            errors = "Login or password are wrong."
            return render_to_response('accounts/login.html',
                                      {'form': login_form, "errors": errors}, context)
    else:
        return render_to_response('accounts/login.html',
                                  {'form': login_form}, context)


def logout(request):
    auth.logout(request)
    return redirect('/index/')


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
