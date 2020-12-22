from common.dict.dicts import SeparatorDict, StringCharacterDict, SchemeColumnTypeDict
from common.models import Schemas, SchemeColumns
from django.db import transaction, IntegrityError
from random import randint


def create_or_update_schema(data, request, schema=None):
    """ Function for create or update schemas """
    with transaction.atomic():
        try:
            if not schema:
                schema = Schemas()
                schema.owner = request.user
            if not data["title"]:
                raise ValueError
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
                if not col["name"] and not col["type"]:
                    raise ValueError
                column.name = col["name"]
                column.type = SchemeColumnTypeDict.objects.get(id=col["type"])

                check_validate_range_inputs(col["input_from"], col["input_to"], column.type.code)

                column.input_from = col["input_from"] if col["input_from"] != '' else None
                column.input_to = col["input_to"] if col["input_to"] != '' else None
                column.order_id = col["order_id"]
                column.save()
            return schema
        except Exception as e:
            raise IntegrityError


def check_validate_range_inputs(input_from, input_to, _type):
    """ Function for validations range from and to integer value """
    if _type != 'integer':
        return True
    if input_from is None or input_to is None:
        raise ValueError
    randint(int(input_from), int(input_to))
    return True
