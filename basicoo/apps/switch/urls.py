from django.conf.urls import url
from .views import (
    SwitchView, UpdateSwitch)

urlpatterns = [
    url(r'^switch/$', SwitchView.as_view(), name='create-switch'),

    url(
        r'^update-switch/(?P<pk>[0-9]+)/$',
        UpdateSwitch.as_view(),
        name='update-switch'
    ),
]
