# -*- coding: UTF-8  -*-
from __future__ import unicode_literals

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, Layout

from .models import Coins, CatalogCoins


class CoinsForm(forms.ModelForm):

    class Meta:
        model = CatalogCoins
        fields = ("country", "currency", "face_value", "metal",
                  "ruler", "number", "circulation", "description") 

    def __init__(self, *args, **kwargs):
        super(CoinsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-4'
        button = Button('send_button', 'Create')
        button.input_type = 'submit'
        button.field_classes = 'btn btn-success form-control'
        self.helper.add_input(button)