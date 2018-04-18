from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ExtraUserField(models.Model):
    user = models.ForeignKey(
        User)
    address = models.CharField(
        max_length=254,
        blank=True,
        null=True)
    city = models.CharField(
        max_length=254,
        blank=True,
        null=True)
    country = models.CharField(
        max_length=254,
        blank=True,
        null=True)
    postalcode = models.CharField(
        max_length=254,
        blank=True,
        null=True)
    token = models.CharField(
        max_length=254,
        blank=True,
        null=True)

    def __str__(self):
        return str(self.user.username).title()
