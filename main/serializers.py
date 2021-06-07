from abc import abstractmethod

from django.contrib.auth.models import User
from rest_framework import serializers

from main.models import UserDevice, AbstractDevice, Capability


class AbstractDeviceSerializer(serializers.ModelSerializer):
    manufacturer = serializers.CharField()

    class Meta:
        model = AbstractDevice
        fields = ("manufacturer", "model", "hw_version", "sw_version")


class CapabilitySerializer(serializers.ModelSerializer):
    type = serializers.CharField(source="get_type_display")

    class Meta:
        model = Capability
        fields = ("type", "retrievable", "parameters",)


class PropertySerializer(serializers.ModelSerializer):
    type = serializers.CharField(source="get_type_display")

    class Meta:
        model = Capability
        fields = ("type", "retrievable", "parameters",)


class DeviceSerializer(serializers.ModelSerializer):
    id = serializers.CharField()
    type = serializers.CharField(source="device.type")
    capabilities = CapabilitySerializer(many=True, source="device.capabilities")
    properties = PropertySerializer(many=True, source="device.properties")
    device_info = AbstractDeviceSerializer(source="device")
    room = serializers.CharField(source="room.name")

    class Meta:
        model = UserDevice
        exclude = ("user", "device")


class PayloadSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(source="id")
    devices = DeviceSerializer(many=True)

    class Meta:
        model = User
        fields = ("user_id", "devices")


class DevicesSerializer(serializers.Serializer):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/reference/get-devices.html
    """

    request_id = serializers.CharField()
    payload = serializers.SerializerMethodField()

    @abstractmethod
    def get_payload(self, obj):
        return PayloadSerializer(obj["user"]).data
