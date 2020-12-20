from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from common.models import DataSet, Schemas


def do_download_dataset_file_view(request, schema_pk, data_pk):
    """ Function for download data sets """
    try:
        schema = get_object_or_404(Schemas, pk=schema_pk)
        if schema.owner != request.user:
            raise PermissionDenied
        data_file = DataSet.objects.get(schemas=schema, id=data_pk)
        response = HttpResponse(content=data_file.file, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename={0}'.format(data_file.file.name)
        return response
    except (DataSet.DoesNotExist, ValueError, TypeError) as e:
        raise Http404
