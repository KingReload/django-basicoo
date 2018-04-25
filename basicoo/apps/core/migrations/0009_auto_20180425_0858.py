# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-25 08:58
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20180423_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitestyle',
            name='button_hover_color',
            field=colorfield.fields.ColorField(blank=True, max_length=18, null=True),
        ),
        migrations.AddField(
            model_name='websitestyle',
            name='navbar_text_hover',
            field=colorfield.fields.ColorField(blank=True, max_length=18, null=True),
        ),
    ]
