from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'base.html'


class RelatedMixin(object):
    list_select_related = []
    list_prefetch_related = []
   
    def get_queryset(self):
        qs = super().get_queryset()
        if self.list_select_related:
            qs = qs.select_related(*self.list_select_related)
        if self.list_prefetch_related:
            qs = qs.prefetch_related(*self.list_prefetch_related)
        return qs


class GetListOrCreateSerializerMixin(object):
    serializer_class = ''
    serializer_class_for_create = ''
    

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.serializer_class 
        return self.serializer_class_for_create

