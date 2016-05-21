# -*- coding: UTF-8  -*-
from __future__ import unicode_literals

from django import forms

from captcha.fields import CaptchaField

from .models import User


class LoginForm(forms.ModelForm):

    button_name = 'Confirm'
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ("username", "password")


class UserForm(forms.ModelForm):

    button_name = 'Confirm'
    captcha = CaptchaField()

    class Meta:
        model = User
