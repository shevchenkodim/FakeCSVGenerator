from django.contrib import admin
from common.models import Schemas, SchemeColumns, DataSet
from common.dict.dicts import SeparatorDict, StringCharacterDict, SchemeColumnTypeDict, CeleryStatusTypeDict


admin.site.register(Schemas)
admin.site.register(DataSet)
admin.site.register(SchemeColumns)
admin.site.register(SeparatorDict)
admin.site.register(StringCharacterDict)
admin.site.register(SchemeColumnTypeDict)
admin.site.register(CeleryStatusTypeDict)
