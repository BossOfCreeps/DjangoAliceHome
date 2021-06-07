from django.contrib import admin

from main.models import Manufacturer, Capability, Room, UserDevice, AbstractDevice

admin.site.register(Manufacturer)
admin.site.register(Capability)
admin.site.register(Room)
admin.site.register(UserDevice)
admin.site.register(AbstractDevice)
