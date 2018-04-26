# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-25 11:31
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20180425_0858'),
    ]

    operations = [
        migrations.RenameField(
            model_name='websitestyle',
            old_name='navbar_text_hover',
            new_name='button_text_hover_color',
        ),
        migrations.AddField(
            model_name='websitestyle',
            name='navbar_hover_color',
            field=colorfield.fields.ColorField(
                blank=True,
                max_length=18,
                null=True),
        ),
        migrations.AddField(
            model_name='websitestyle',
            name='navbar_text_hover_color',
            field=colorfield.fields.ColorField(
                blank=True,
                max_length=18,
                null=True),
        ),
    ]
