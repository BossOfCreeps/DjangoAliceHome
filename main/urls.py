"""DjangoAliceHome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from main.views import Check, Devices, Action, Query

"""
https://yandex.ru/dev/dialogs/smart-home/doc/reference/resources.html
"""
urlpatterns = [
    path('', Check.as_view(), name='availability'),
    path('user/devices', Devices.as_view(), name='devices'),
    path('user/devices/action', Action.as_view(), name='action'),
    path('user/devices/query', Query.as_view(), name='action'),
]
