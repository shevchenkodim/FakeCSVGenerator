import json

from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from rest_framework.status import HTTP_200_OK
from broker.services.schemas import create_or_update_schema
from client_front.view.schema_edit_view import add_dicts_to_context


@method_decorator(login_required, name='dispatch')
class SchemaCreateView(TemplateView):
    """Page for create schema """
    template_name = "schemas/create_or_edit.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["schema"] = None
        context["title"] = "New schema"
        context["schema_data"] = {"id": "", "title": "", "separator_id": "", "character_id": ""}
        context["columns"] = []
        context = add_dicts_to_context(**context)
        return context

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode())
            schema = create_or_update_schema(schema=None, data=data, request=request)
        except (KeyError, ValueError, IntegrityError) as e:
            return JsonResponse({"status": "no", "error": "Error! Please try again!"}, status=HTTP_200_OK)
        return JsonResponse({
            "status": "ok",
            "redirect": reverse('client_front:schema_data_sets', kwargs={"schema_pk": schema.id})
        }, status=HTTP_200_OK)
