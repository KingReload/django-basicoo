# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-25 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20180425_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websitestyle',
            name='template_name',
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                unique=True),
        ),
    ]
