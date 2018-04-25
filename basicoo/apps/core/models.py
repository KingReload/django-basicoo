from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from colorfield.fields import ColorField

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


class WebsiteStyle(models.Model):
    navbar_gradient = models.CharField(
        max_length=254,
        blank=True,
        null=True)
    navbar_text_color = ColorField(
        max_length=254,
        blank=True,
        null=True)
    navbar_hover_color = ColorField(
        max_length=254,
        blank=True,
        null=True)
    navbar_text_hover_color = ColorField(
        max_length=254,
        blank=True,
        null=True)
    body_gradient = models.CharField(
        max_length=254,
        blank=True,
        null=True)
    body_text_color = ColorField(
        max_length=254,
        blank=True,
        null=True)
    footer_color = ColorField(
        max_length=254,
        blank=True,
        null=True)
    footer_text_color = ColorField(
        max_length=254,
        blank=True,
        null=True)
    button_color = ColorField(
        max_length=254,
        blank=True,
        null=True)
    button_text_color = ColorField(
        max_length=254,
        blank=True,
        null=True)
    button_hover_color = ColorField(
        max_length=254,
        blank=True,
        null=True)
    button_text_hover_color = ColorField(
        max_length=254,
        blank=True,
        null=True)

    save_template = models.BooleanField(
        default=False)
    template_name = models.CharField(
        unique=True,
        max_length=255,
        blank=True,
        null=True)

    def __str__(self):
        name = self.template_name
        
        if name is not None:
            return str(name).title()
        else:
            return str(self.id).title()
