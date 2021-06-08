from django.contrib.auth.models import User
from django.db import models
from polymorphic.models import PolymorphicModel

from main.constants import CAPABILITIES, PROPERTIES, DEVICE_TYPES


class Manufacturer(models.Model):
    name = models.CharField("Производитель", max_length=1024)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = verbose_name_plural = "Производитель"


class AbstractDevice(PolymorphicModel):
    manufacturer = models.ForeignKey(Manufacturer, models.PROTECT, "devices", verbose_name="Производитель")
    model = models.CharField("Название модели", max_length=1024)
    type = models.CharField("Тип", choices=DEVICE_TYPES, max_length=64)
    hw_version = models.CharField("Версия аппартаной части", max_length=256)
    sw_version = models.CharField("Версия программной части", max_length=256)

    def __str__(self):
        return f"{self.manufacturer} {self.model}"

    class Meta:
        verbose_name = verbose_name_plural = "Абстрактное устройство"


class Capability(models.Model):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/capability-types.html
    """
    device = models.ForeignKey(AbstractDevice, models.CASCADE, "capabilities", verbose_name="Устройство")
    type = models.CharField("Тип", choices=CAPABILITIES, max_length=64)
    retrievable = models.BooleanField("Извлекаемый", default=True)
    reportable = models.BooleanField("Отчетно", default=True)
    parameters = models.JSONField("Параметры", blank=True, null=True)

    def __str__(self):
        return f"{self.type} {self.device}"

    class Meta:
        verbose_name = verbose_name_plural = "Умение устройства"


class CapabilityState(models.Model):
    capability = models.OneToOneField(Capability, models.CASCADE, related_name="state", verbose_name="Умение")
    instance = models.CharField("Единица измерения", max_length=256)
    value = models.JSONField("Состояние")

    def __str__(self):
        return f"{self.capability} {self.instance}"

    class Meta:
        verbose_name = verbose_name_plural = "Состояние умения устройства"


class Property(models.Model):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/properties-types.html
    """
    device = models.ForeignKey(AbstractDevice, models.CASCADE, "properties", verbose_name="Устройство")
    type = models.CharField("Тип", choices=PROPERTIES, max_length=64)
    retrievable = models.BooleanField("Извлекаемый", default=True)
    reportable = models.BooleanField("Отчетно", default=True)
    parameters = models.JSONField("Параметры", blank=True, null=True)

    def __str__(self):
        return f"{self.type} {self.device}"

    class Meta:
        verbose_name = verbose_name_plural = "Датчик устройства"


class Room(models.Model):
    name = models.CharField("Комната", max_length=1024)
    user = models.ForeignKey(User, models.CASCADE, "rooms")

    def __str__(self):
        return f"{self.user} {self.name}"

    class Meta:
        verbose_name = verbose_name_plural = "Комната"


class UserDevice(models.Model):
    user = models.ForeignKey(User, models.CASCADE, "devices", verbose_name="Пользователь")
    name = models.CharField("Название устройства", max_length=1024)
    description = models.TextField("Описание", null=True, blank=True)
    room = models.ForeignKey(Room, models.PROTECT, "devices", verbose_name="Комната", null=True, blank=True)
    device = models.ForeignKey(AbstractDevice, models.PROTECT, "user_devices", verbose_name="Устройство")
    custom_data = models.JSONField(null=True, blank=True)
    device_info = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = verbose_name_plural = "Устройства пользователя"
