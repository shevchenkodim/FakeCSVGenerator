from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from broker.decorators import owner_access_to_schema
from common.models import DataSet, Schemas

decorators = [login_required, owner_access_to_schema]


@method_decorator(decorators, name='dispatch')
class DataSetsView(TemplateView):
    """ Schema data sets page """
    template_name = "data_set/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["schema_data_sets"] = DataSet.objects.filter(schemas=kwargs["schema"])
        context["schema"] = kwargs["schema"]
        return context
