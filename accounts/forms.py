# -*- coding: UTF-8  -*-
from __future__ import unicode_literals

from django import forms

from captcha.fields import CaptchaField

from core.forms import CrispyMixin

from .models import User


class UserForm(CrispyMixin, forms.ModelForm):

    button_name = 'Confirm'
    captcha = CaptchaField()

    class Meta:
        model = User
        exclude = ('user', )
