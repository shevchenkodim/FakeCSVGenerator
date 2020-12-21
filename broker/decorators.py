from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from common.models import Schemas


def owner_access_to_schema(view_func):
    """ Decorators for check schemas owner """
    def wrap(request, *args, **kwargs):
        try:
            schema = get_object_or_404(Schemas, pk=kwargs["schema_pk"])
            kwargs["schema"] = schema
            if schema.owner != request.user:
                raise PermissionDenied
            return view_func(request, *args, **kwargs)
        except (KeyError, ValueError):
            return redirect(reverse('client_front:index'))
    return wrap
