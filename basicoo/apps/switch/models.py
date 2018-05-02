from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Switch(models.Model):

    app1 = models.CharField(
        max_length=255,
        blank=True,
        null=True)

    def __str__(self):
        return str(self.app1).title()
