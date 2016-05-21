# -*- coding: UTF-8  -*-


class AngularMixin(object):

    def __init__(self, *args, **kwargs):
        super(AngularMixin, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'ng-model': field,
            })
