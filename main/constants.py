"""
https://yandex.ru/dev/dialogs/smart-home/doc/concepts/device-types.html
"""
DEVICE_TYPES = [
    ("devices.types.light", "light"),
    ("devices.types.socket", "socket"),
    ("devices.types.switch", "switch"),
    ("devices.types.thermostat", "thermostat"),
    ("devices.types.thermostat.ac", "thermostat_ac"),
    ("devices.types.media_device", "media_device"),
    ("devices.types.media_device.tv", "media_device_tv"),
    ("devices.types.media_device.tv_box", "media_device_tv_box"),
    ("devices.types.media_device.receiver", "media_device_receiver"),
    ("devices.types.cooking", "cooking"),
    ("devices.types.cooking.coffee_maker", "cooking_coffee_maker"),
    ("devices.types.cooking.kettle", "cooking_kettle"),
    ("devices.types.cooking.multicooker", "cooking_multicooker"),
    ("devices.types.openable", "openable"),
    ("devices.types.openable.curtain", "openable_curtain"),
    ("devices.types.humidifier", "humidifier"),
    ("devices.types.purifier", "purifier"),
    ("devices.types.vacuum_cleaner", "vacuum_cleaner"),
    ("devices.types.washing_machine", "washing_machine"),
    ("devices.types.dishwasher", "dishwasher"),
    ("devices.types.iron", "iron"),
    ("devices.types.sensor", "sensor"),
    ("devices.types.other", "other"),
]

CAPABILITIES = [
    ("on_off", "devices.capabilities.on_off"),
    ("color_setting", "devices.capabilities.color_setting"),
    ("mode", "devices.capabilities.mode"),
    ("range", "devices.capabilities.range"),
    ("toggle", "devices.capabilities.toggle"),
]

PROPERTIES = [
    ("amperage", "devicesamperage"),
    ("battery_level", "battery_level"),
    ("co2_level", "co2_level"),
    ("humidity", "humidity"),
    ("illumination", "illumination"),
    ("power", "power"),
    ("pressure", "pressure"),
    ("temperature", "temperature"),
    ("voltage", "voltage"),
    ("water_level_float", "water_level_float"),

    ("vibration", "vibration"),
    ("open", "open"),
    ("button", "button"),
    ("motion", "motion"),
    ("smoke", "smoke"),
    ("gas", "gas"),
    ("battery_level", "battery_level"),
    ("water_level_event", "water_level_event"),
    ("water_leak", "water_leak"),
]
