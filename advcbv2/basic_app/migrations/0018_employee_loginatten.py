# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-26 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0017_auto_20170525_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='loginatten',
            field=models.CharField(default='x', max_length=256),
        ),
    ]