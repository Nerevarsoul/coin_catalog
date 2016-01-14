# -*- coding: UTF-8  -*-
from __future__ import unicode_literals

from django import forms

from ajax_select.fields import AutoCompleteSelectField, AutoCompleteSelectMultipleField
from captcha.fields import CaptchaField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, Layout

from .models import Coins, CatalogCoins, UserProfile


class CrispyMixin(object):

    def __init__(self, *args, **kwargs):
        super(CrispyMixin, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-4'
        button = Button('send_button', self.button_name)
        button.input_type = 'submit'
        button.field_classes = 'btn btn-success form-control'
        self.helper.add_input(button)


class CatalogCoinsForm(CrispyMixin, forms.ModelForm):

    button_name = 'Create'

    class Meta:
        model = CatalogCoins
        fields = ("country", "currency", "face_value", "metal",
                  "ruler", "number", "circulation", "description") 


class UserProfileForm(CrispyMixin, forms.ModelForm):

    button_name = 'Confirm'
    captcha = CaptchaField()

    class Meta:
        model = UserProfile
        exclude = ('user', )


class CoinsForm(CrispyMixin, forms.ModelForm):

    button_name = 'Create'
    
    catalog_coin = AutoCompleteSelectField('catalog_coin',
                                           label="Монета",
                                           required=False,
                                           help_text=None)

    class Meta:
        model = Coins
        fields = ("condition", "year", "mint", "catalog_coin", "available", 
                  "needful", "changable")
