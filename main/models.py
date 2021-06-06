from django.contrib.auth.models import User
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField("Производитель", max_length=1024)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = verbose_name_plural = "Производитель"


class Type(models.Model):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/device-types.html
    """
    name = models.CharField("Тип", max_length=1024)


class Capability(models.Model):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/capability-types.html
    """
    name = models.CharField("Умение", max_length=1024)


class Property(models.Model):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/properties-types.html
    """
    name = models.CharField("Датчик", max_length=1024)


class AbstractDevice(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, models.PROTECT, "%(class)s", verbose_name="Производитель")
    model = models.CharField("Название модели", max_length=1024)
    hw_version = models.CharField("Версия аппартаной части", max_length=256)
    sw_version = models.CharField("Версия программной части", max_length=256)
    type = models.ForeignKey(Type, models.PROTECT, "%(class)s", verbose_name="Тип")
    capabilities = models.ManyToManyField(Capability, "%(class)s", verbose_name="Умения")
    properties = models.ManyToManyField(Property, "%(class)s", verbose_name="Датчики")

    def __str__(self):
        return f"{self.manufacturer} {self.model}"

    class Meta:
        verbose_name = verbose_name_plural = "Абстрактное устройтсво"


class Button(AbstractDevice):
    pass


class Room(models.Model):
    name = models.CharField("Комната", max_length=1024)
    user = models.ForeignKey(User, models.CASCADE, "rooms")

    def __str__(self):
        return f"{self.user} {self.name}"

    class Meta:
        verbose_name = verbose_name_plural = "Комната"


class UserDevice(models.Model):
    user = models.ForeignKey(User, models.CASCADE, "devices", verbose_name="Пользователь")
    device = models.ForeignKey("AbstractDevice", models.PROTECT, verbose_name="Устройство")
    name = models.CharField("Название устройства", max_length=1024)
    description = models.TextField("Описание", null=True, blank=True)
    room = models.ForeignKey(Room, models.PROTECT, "devices", verbose_name="Комната", null=True, blank=True)

    @property
    def custom_data(self):
        return None

    @property
    def device_info(self):
        return None
