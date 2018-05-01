from django.conf.urls import url
from .views import (
    SwitchHome)

urlpatterns = [
    url(r'^switchhome/$', SwitchHome.as_view(), name='switchhome'),
]
