import json
from django.core.exceptions import PermissionDenied
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_200_OK
from common.models import Schemas


def do_remove_schema(request, schema_pk):
    """ Function for remove scheme """
    try:
        schema = get_object_or_404(Schemas, pk=schema_pk)
        if schema.owner != request.user:
            raise PermissionDenied
        schema.delete()
    except (KeyError, IntegrityError) as e:
        return JsonResponse({"status": "no", "error": "Error! Please try again!"}, status=HTTP_200_OK)
    return JsonResponse({"status": "ok"}, status=HTTP_200_OK)
