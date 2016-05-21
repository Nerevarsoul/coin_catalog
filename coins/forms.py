# -*- coding: UTF-8  -*-
from __future__ import unicode_literals

from django import forms

from ajax_select.fields import AutoCompleteSelectField, AutoCompleteSelectMultipleField
from djng.forms import NgModelFormMixin, NgModelForm

from .models import Coin, CatalogCoin
from core.forms import CrispyMixin


class CatalogCoinsForm(CrispyMixin, forms.ModelForm):

    button_name = 'Create'

    class Meta:
        model = CatalogCoin
        fields = ("country", "currency", "face_value", "metal",
                  "ruler", "number", "circulation", "description") 


class CoinsForm(NgModelFormMixin, NgModelForm):

    button_name = 'Create'
    
    catalog_coin = AutoCompleteSelectField('catalog_coin',
                                           label="Монета",
                                           required=False,
                                           help_text=None)

    class Meta:
        model = Coin
        fields = ("condition", "year", "mint", "catalog_coin", "available", 
                  "needful", "changable")
