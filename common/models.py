

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from common.dict.dicts import SeparatorDict, StringCharacterDict, SchemeColumnTypeDict, CeleryStatusTypeDict


class Schemas(models.Model):
    """ User schemas model """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    title = models.CharField(verbose_name='Title', max_length=128, blank=False, null=False)
    created_at = models.DateTimeField(verbose_name='Created date', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Updated date', auto_now_add=True)
    col_separator = models.ForeignKey(SeparatorDict, on_delete=models.PROTECT, verbose_name='Separator')
    col_string_char = models.ForeignKey(StringCharacterDict, on_delete=models.PROTECT, verbose_name='String character')

    class Meta:
        ordering = ['-updated_at']
        db_table = 'schemas'

    def __str__(self):
        return self.title

    def get_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "separator_id": self.col_separator.id,
            "character_id": self.col_string_char.id
        }

    def get_absolute_url(self):
        return reverse('client_front:schema_data_sets', kwargs={'schema_pk': self.id})

    def save(self, *args, **kwargs):
        super(Schemas, self).save(*args, **kwargs)


class SchemeColumns(models.Model):
    """ Scheme columns model """
    schemas = models.ForeignKey(Schemas, on_delete=models.CASCADE, verbose_name='Schemas')
    name = models.CharField(verbose_name='Name', max_length=128)
    type = models.ForeignKey(SchemeColumnTypeDict, on_delete=models.PROTECT, verbose_name='Type')
    input_from = models.IntegerField(null=True, blank=True, verbose_name='From')
    input_to = models.IntegerField(null=True, blank=True, verbose_name='To')
    order_id = models.IntegerField(default=0)

    class Meta:
        ordering = ['order_id']
        db_table = 'scheme_columns'

    def get_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type.id,
            "input_from": self.input_from if self.input_from else '',
            "input_to": self.input_to if self.input_to else '',
            "order_id": self.order_id
        }


class DataSet(models.Model):
    """ Data set model """
    schemas = models.ForeignKey(Schemas, on_delete=models.CASCADE, verbose_name='Schemas')
    created_at = models.DateTimeField(verbose_name='Created date', auto_now_add=True)
    rows = models.IntegerField(verbose_name='Rows', default=0)
    status = models.ForeignKey(CeleryStatusTypeDict, on_delete=models.PROTECT, verbose_name='Status')
    file = models.FileField(upload_to='data_set/', blank=True, null=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'data_set'
