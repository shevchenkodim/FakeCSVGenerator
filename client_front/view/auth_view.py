from audioop import reverse

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.generic import TemplateView


class AuthView(TemplateView):
    """Index auth page"""
    template_name = "auth/index.html"


def client_logout(request):
    """ User logout view """
    logout(request)
    return redirect('/auth')
