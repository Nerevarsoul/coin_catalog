from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'base.html'


class GetListOrCreateSerializerMixin(object):
    serializer_class = ''
    serializer_class_for_create = ''
    

    def get_serializer_class(self):
        if self.method == 'GET':
            return serializer_class 
        return serializer_class_for_create

