from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import login, authenticate


@api_view(['POST'])
def client_auth_api_view(request):
    """ Client Auth """
    username = request.data.get("username", None)
    password = request.data.get("password", None)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        return Response({"status": "no", "error": "Login error! Check the login details!"}, status=status.HTTP_200_OK)
    return Response({"status": "ok", "redirect": reverse('client_front:index')}, status=status.HTTP_200_OK)
