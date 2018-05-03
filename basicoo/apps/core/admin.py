from django.contrib import admin
from django.contrib.auth.models import Permission

from .models import (
    ExtraUserField, Log, WebsiteStyle)


# Django models
admin.site.register(Permission)


# Custom models
admin.site.register(ExtraUserField)
admin.site.register(Log)
admin.site.register(WebsiteStyle)
