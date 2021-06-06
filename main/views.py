from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class Availability(APIView):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/reference/check.html
    """

    def get(self, request, *args, **kwargs):
        return Response("")


class Devices(APIView):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/reference/get-devices.html
    """

    def get(self, request, *args, **kwargs):
        return Response("")
