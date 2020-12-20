from __future__ import absolute_import
from celery import shared_task
from broker.services.generate_csv import generate_csv_for_schema


@shared_task
def generate_csv_for_schema_task(obj_id):
    generate_csv_for_schema(obj_id)
    return True


