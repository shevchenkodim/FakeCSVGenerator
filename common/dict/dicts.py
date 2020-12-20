from django.db import models


class Dictionaries(models.Model):
    """ Base Abstract Dict Model """
    code = models.CharField(max_length=255, unique=True)
    value = models.CharField(max_length=255, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.code} ({self.value})'


class SeparatorDict(Dictionaries):
    """ Separator dict for schemas """

    class Meta:
        db_table = 'dict_separator'


class StringCharacterDict(Dictionaries):
    """ String character dict for schemas """

    class Meta:
        db_table = 'dict_string_character'


class SchemeColumnTypeDict(Dictionaries):
    """ Scheme column type """

    class Meta:
        db_table = 'dict_scheme_column_type'


class CeleryStatusTypeDict(Dictionaries):
    """ Celery status type """

    class Meta:
        db_table = 'dict_celery_status_type'
