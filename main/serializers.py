from abc import abstractmethod

from django.contrib.auth.models import User
from rest_framework import serializers

from main.models import Capability, Property, CapabilityState, AbstractDevice, UserDevice


class CapabilityStateSerializer(serializers.ModelSerializer):
    instance = serializers.CharField()
    action_result = serializers.SerializerMethodField()
    value = serializers.CharField()

    def get_action_result(self, obj):
        return {"status": "DONE"}

    class Meta:
        model = CapabilityState
        fields = ("instance", "value", "action_result")


class CapabilitySerializer(serializers.ModelSerializer):
    type = serializers.CharField(source="get_type_display")
    state = CapabilityStateSerializer()

    class Meta:
        model = Capability
        fields = ("type", "state", "retrievable", "parameters",)


class PropertySerializer(serializers.ModelSerializer):
    type = serializers.CharField(source="get_type_display")

    class Meta:
        model = Property
        fields = ("type", "retrievable", "parameters",)


class AbstractDeviceSerializer(serializers.ModelSerializer):
    manufacturer = serializers.CharField()

    class Meta:
        model = AbstractDevice
        fields = ("manufacturer", "model", "hw_version", "sw_version")


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
    request_id = serializers.CharField()
    payload = serializers.SerializerMethodField()

    @abstractmethod
    def get_payload(self, obj):
        return PayloadSerializer(obj["user"]).data


