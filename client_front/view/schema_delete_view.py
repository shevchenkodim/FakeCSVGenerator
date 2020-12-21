import json
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_200_OK
from broker.decorators import owner_access_to_schema
from common.models import Schemas


@owner_access_to_schema
@login_required
def do_remove_schema(request, schema_pk, **kwargs):
    """ Function for remove scheme """
    try:
        schema = kwargs["schema"]
        schema.delete()
    except (KeyError, IntegrityError) as e:
        return JsonResponse({"status": "no", "error": "Error! Please try again!"}, status=HTTP_200_OK)
    return JsonResponse({"status": "ok"}, status=HTTP_200_OK)
