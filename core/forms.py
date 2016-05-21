# -*- coding: UTF-8  -*-
from __future__ import unicode_literals

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, Layout


class CrispyMixin(object):

    def __init__(self, *args, **kwargs):
        super(CrispyMixin, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'ng-model': field,
            })

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

