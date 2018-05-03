from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from colorfield.fields import ColorField

# Create your models here.


class ExtraUserField(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
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
    template = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text=(
            'Select one of the templates you want to use.' +
            'You can also choose not to select any template.'))
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
        default=False,
        help_text=(
            'Do you want to save the template?' +
            ' Yes / No'))
    template_name = models.CharField(
        unique=True,
        max_length=255,
        blank=True,
        null=True,
        help_text='Set a templatename for the template.')
    template_css_field = models.TextField(
        blank=True,
        null=True)

    def __str__(self):
        name = self.template_name

        if name is not None:
            return str(name).title()
        else:
            return str(self.id).title()


class Log(models.Model):
    log_action = models.CharField(
        max_length=255,
        null=True,
        blank=True)
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True)
    log = models.TextField()
    datetime = models.DateTimeField(
        auto_now=True)

    def __str__(self):
        return str(self.log_action).title()
