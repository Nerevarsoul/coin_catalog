# -*- coding: UTF-8  -*-
from __future__ import unicode_literals

from django import forms

from ajax_select.fields import AutoCompleteSelectField, AutoCompleteSelectMultipleField
from djng.forms import NgModelFormMixin, NgForm

from core.forms import CrispyMixin

from .models import Coin, CatalogCoin


class CatalogCoinsForm(CrispyMixin, forms.ModelForm):

    button_name = 'Create'

    class Meta:
        model = CatalogCoin
        fields = ("country", "currency", "face_value", "metal",
                  "ruler", "number", "circulation", "description") 


class CoinsForm(CrispyMixin, forms.ModelForm):

    button_name = 'Create'
    
    catalog_coin = AutoCompleteSelectField('catalog_coin',
                                           label="Монета",
                                           required=False,
                                           help_text=None)

    class Meta:
        model = Coin
        fields = ("condition", "year", "mint", "catalog_coin", "available", 
                  "needful", "changable")
