import json

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db import IntegrityError, transaction
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_200_OK
from broker.decorators import owner_access_to_schema
from broker.tasks import generate_csv_for_schema_task
from common.dict.dicts import CeleryStatusTypeDict
from common.models import Schemas, DataSet
from django.db import transaction


@owner_access_to_schema
@login_required
def do_generate_dataset_file_view(request, schema_pk, **kwargs):
    """ Function for generate new sets for schema """
    try:
        # with transaction.atomic():
        #     try:
        schema = kwargs["schema"]
        data = json.loads(request.body.decode())
        rows = data["rows"]

        obj = DataSet()
        obj.schemas = schema
        obj.rows = rows
        obj.status = CeleryStatusTypeDict.objects.get_or_create(code='processing', value='Processing')[0]
        obj.save()

        print(obj)
        print(obj.id)

        transaction.commit()

        generate_csv_for_schema_task.delay(obj.id)

            # except Exception as e:
            #     print(e)
            #     raise IntegrityError
    except (KeyError, IntegrityError) as e:
        return JsonResponse({"status": "no", "error": "Invalid data"}, status=HTTP_200_OK)
    return JsonResponse({"status": "ok"}, status=HTTP_200_OK)
