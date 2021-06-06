from django.contrib import admin
from main.models import AbstractDevice, Manufacturer, Type, Capability, Property, Button, Room, UserDevice

admin.site.register(AbstractDevice)
admin.site.register(Manufacturer)
admin.site.register(Type)
admin.site.register(Capability)
admin.site.register(Property)
admin.site.register(Button)
admin.site.register(Room)
admin.site.register(UserDevice)
