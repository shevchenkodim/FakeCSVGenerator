from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from common.models import DataSet, Schemas


@method_decorator(login_required, name='dispatch')
class DataSetsView(TemplateView):
    """ Schema data sets page """
    template_name = "data_set/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        schema = get_object_or_404(Schemas, pk=self.kwargs['schema_pk'])
        if schema.owner != self.request.user:
            raise PermissionDenied
        context["schema_data_sets"] = DataSet.objects.filter(schemas=schema)
        context["schema"] = schema
        return context
