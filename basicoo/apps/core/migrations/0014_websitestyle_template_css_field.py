# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-26 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_websitestyle_template'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitestyle',
            name='template_css_field',
            field=models.TextField(blank=True, null=True),
        ),
    ]
