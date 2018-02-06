from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'base.html'


class GetListOrCreateSerializerMixin(object):
    serializer_class = ''
    serializer_class_for_create = ''

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.serializer_class 
        return self.serializer_class_for_create
