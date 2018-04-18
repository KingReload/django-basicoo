from django.contrib import admin
from django.contrib.auth.models import Permission

from .models import (
    ExtraUserField)


# Django models
admin.site.register(Permission)


# Custom models
admin.site.register(ExtraUserField)
