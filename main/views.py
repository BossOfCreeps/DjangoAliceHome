from pprint import pprint

from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import AbstractDevice, UserDevice
from main.serializers import DevicesSerializer


def get_id(request):
    return request.headers["X-Request-Id"] if "X-Request-Id" in request.headers else ""


class Check(APIView):
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
        return Response(DevicesSerializer({"request_id": get_id(request), "user": request.user}).data)


class Action(APIView):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/reference/post-action.html
    """

    def post(self, request, *args, **kwargs):
        for device_dict in request.data["payload"]["devices"]:
            device = UserDevice.objects.get(id=device_dict["id"])
            for dict_c in device_dict["capabilities"]:
                for dev_c in device.device.capabilities.all():
                    if dev_c.get_type_display() == dict_c["type"]:
                        print(f'{device} параметр {dict_c["state"]["instance"]} в значение {dict_c["state"]["value"]}')
                        dev_c.state.instance = dict_c["state"]["instance"]
                        dev_c.state.value = dict_c["state"]["value"]
                        dev_c.state.save()

        return Response(DevicesSerializer({"request_id": get_id(request), "user": request.user}).data)
