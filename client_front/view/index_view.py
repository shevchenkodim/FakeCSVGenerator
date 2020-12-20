from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from common.models import Schemas


@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    """Index schemas page"""
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["schemas_list"] = Schemas.objects.filter(owner=self.request.user)
        return context
