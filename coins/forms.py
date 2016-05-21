# -*- coding: UTF-8  -*-
from django import forms

from .models import Coin, CatalogCoin
from core.forms import AngularMixin


class CatalogCoinsForm(AngularMixin, forms.ModelForm):

    button_name = 'Create'

    class Meta:
        model = CatalogCoin
        fields = ("country", "currency", "face_value", "metal",
                  "ruler", "number", "circulation", "description") 


class CoinsForm(AngularMixin, forms.ModelForm):

    button_name = 'Create'
    
    # catalog_coin = AutoCompleteSelectField('catalog_coin',
    #                                        label="Монета",
    #                                        required=False,
    #                                        help_text=None)

    class Meta:
        model = Coin
        fields = ("condition", "year", "mint", "catalog_coin", "available", 
                  "needful", "changable")
