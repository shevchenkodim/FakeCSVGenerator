from common.dict.dicts import SeparatorDict, StringCharacterDict, SchemeColumnTypeDict
from common.models import Schemas, SchemeColumns
from django.db import transaction, IntegrityError


def create_or_update_schema(data, request, schema=None):
    """ Function for create or update schemas """
    with transaction.atomic():
        try:
            if not schema:
                schema = Schemas()
                schema.owner = request.user
            schema.title = data["title"]
            schema.col_separator = SeparatorDict.objects.get(id=data["character_id"])
            schema.col_string_char = StringCharacterDict.objects.get(id=data["separator_id"])
            schema.save()
            for col in data["columns"]:
                try:
                    column = SchemeColumns.objects.get(schemas=schema, id=col.get("id", None))
                except (ValueError, KeyError, SchemeColumns.DoesNotExist):
                    column = SchemeColumns()
                    column.schemas = schema
                column.name = col["name"]
                column.type = SchemeColumnTypeDict.objects.get(id=col["type"])
                column.input_from = col["input_from"] if col["input_to"] != '' else None
                column.input_to = col["input_to"] if col["input_to"] != '' else None
                column.order_id = col["order_id"]
                column.save()
            return schema
        except Exception as e:
            raise IntegrityError
