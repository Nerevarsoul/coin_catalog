# -*- coding: UTF-8  -*-
from __future__ import unicode_literals

from django import forms

from captcha.fields import CaptchaField

from core.forms import CrispyMixin

from .models import User


class LoginForm(CrispyMixin, forms.ModelForm):

    button_name = 'Confirm'
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ("username", "password")


class UserForm(CrispyMixin, forms.ModelForm):

    button_name = 'Confirm'
    captcha = CaptchaField()

    class Meta:
        model = User
