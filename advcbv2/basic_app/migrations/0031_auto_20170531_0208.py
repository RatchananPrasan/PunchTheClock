# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-30 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0030_auto_20170530_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(null=True),
        ),
    ]
