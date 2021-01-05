from __future__ import absolute_import
from fake_csv.celery import app
from broker.services.generate_csv import generate_csv_for_schema
from celery import shared_task


@shared_task
def generate_csv_for_schema_task(obj_id):
    res = generate_csv_for_schema(obj_id)
    return res
