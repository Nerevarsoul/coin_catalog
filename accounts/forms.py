# -*- coding: UTF-8  -*-
from __future__ import unicode_literals

from django import forms

from core.forms import CrispyMixin

from .models import UserProfile


class UserProfileForm(CrispyMixin, forms.ModelForm):

    button_name = 'Confirm'
    captcha = CaptchaField()

    class Meta:
        model = UserProfile
        exclude = ('user', )
