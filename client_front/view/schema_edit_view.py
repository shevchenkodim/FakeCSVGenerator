import json
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from rest_framework.status import HTTP_200_OK

from broker.services.schemas import create_or_update_schema
from common.dict.dicts import SeparatorDict, StringCharacterDict, SchemeColumnTypeDict
from common.models import Schemas, SchemeColumns


@method_decorator(login_required, name='dispatch')
class SchemaEditView(TemplateView):
    """Schema edit page"""
    template_name = "schemas/create_or_edit.html"

    def get_context_data(self, **kwargs):
        schema = get_object_or_404(Schemas, pk=self.kwargs['schema_pk'])
        if schema.owner != self.request.user:
            raise PermissionDenied
        context = super().get_context_data(**kwargs)
        context["schema"] = schema
        context["title"] = f"Edit schema {schema.title}"
        context["schema_data"] = schema.get_json()
        context["columns"] = [col.get_json() for col in SchemeColumns.objects.filter(schemas=schema)]
        context["column_separator"] = SeparatorDict.objects.all()
        context["string_character"] = StringCharacterDict.objects.all()
        context["column_types"] = SchemeColumnTypeDict.objects.all()
        context["integer_type_id"] = SchemeColumnTypeDict.objects.get_or_create(code='integer', value='Integer')[0].id
        return context

    def post(self, request, *args, **kwargs):
        schema = get_object_or_404(Schemas, pk=self.kwargs['schema_pk'])
        if schema.owner != request.user:
            raise PermissionDenied
        try:
            data = json.loads(request.body.decode())
            schema = create_or_update_schema(schema=schema, data=data, request=request)
        except (KeyError, ValueError, IntegrityError) as e:
            return JsonResponse({"status": "no", "error": "Error! Please try again!"}, status=HTTP_200_OK)
        return JsonResponse({
            "status": "ok",
            "redirect": reverse('client_front:schema_data_sets', kwargs={"schema_pk": schema.id})
        }, status=HTTP_200_OK)


@login_required
def create_column_for_scheme(request, schema_pk):
    """ Function create new column for schema """
    try:
        schema = get_object_or_404(Schemas, pk=schema_pk)
        if schema.owner != request.user:
            raise PermissionDenied
        data = json.loads(request.body.decode())
        column = SchemeColumns.objects.create(
            schemas=schema,
            name=data["name"],
            type=get_object_or_404(SchemeColumnTypeDict, pk=data["type"]),
            input_from=int(data["input_from"]) if data["input_from"] else None,
            input_to=int(data["input_to"]) if data["input_to"] else None,
            order_id=data["order_id"]
        )
    except (KeyError, IntegrityError) as e:
        return JsonResponse({"status": "no", "error": "Invalid data"}, status=HTTP_200_OK)
    return JsonResponse({"status": "ok", "column": column.get_json()}, status=HTTP_200_OK)


@login_required
def remove_column_in_scheme(request, schema_pk):
    """ Function for remove column in schema """
    try:
        schema = get_object_or_404(Schemas, pk=schema_pk)
        if schema.owner != request.user:
            raise PermissionDenied
        data = json.loads(request.body.decode())
        column = SchemeColumns.objects.filter(schemas=schema, id=data["col_id"])
        column.delete()
    except (KeyError, IntegrityError) as e:
        return JsonResponse({"status": "no", "error": "Error! Please try again!"}, status=HTTP_200_OK)
    return JsonResponse({"status": "ok"}, status=HTTP_200_OK)
