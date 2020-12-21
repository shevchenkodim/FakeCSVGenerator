from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from broker.decorators import owner_access_to_schema
from common.models import DataSet


@owner_access_to_schema
@login_required
def do_download_dataset_file_view(request, schema_pk, data_pk, **kwargs):
    """ Function for download data sets """
    try:
        schema = kwargs["schema"]
        data_file = DataSet.objects.get(schemas=schema, id=data_pk)
        response = HttpResponse(content=data_file.file, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename={0}'.format(data_file.file.name)
        return response
    except (DataSet.DoesNotExist, ValueError, TypeError) as e:
        raise Http404
