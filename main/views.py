from pprint import pprint

from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import AbstractDevice
from main.serializers import DevicesSerializer


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
        request_id = request.headers["X-Request-Id"] if "X-Request-Id" in request.headers else ""
        return Response(DevicesSerializer({"request_id": request_id, "user": request.user}).data)
