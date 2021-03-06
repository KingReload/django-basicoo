# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-20 13:56
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_extrauserfield_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteStyle',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('navbar_gradient', models.CharField(
                    blank=True,
                    max_length=254,
                    null=True)),
                ('navbar_text_color', colorfield.fields.ColorField(
                    blank=True,
                    max_length=18,
                    null=True)),
                ('body_gradient', models.CharField(
                    blank=True,
                    max_length=254,
                    null=True)),
                ('body_text_color', colorfield.fields.ColorField(
                    blank=True,
                    max_length=18,
                    null=True)),
                ('footer_color', colorfield.fields.ColorField(
                    blank=True,
                    max_length=18,
                    null=True)),
                ('footer_text_color', colorfield.fields.ColorField(
                    blank=True,
                    max_length=18,
                    null=True)),
                ('button_gradient', models.CharField(
                    blank=True,
                    max_length=254,
                    null=True)),
                ('button_text_color', colorfield.fields.ColorField(
                    blank=True,
                    max_length=18,
                    null=True)),
            ],
        ),
    ]
