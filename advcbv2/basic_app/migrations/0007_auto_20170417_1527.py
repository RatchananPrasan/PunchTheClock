# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-17 15:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0006_auto_20170417_1524'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='profile_pic',
            new_name='profile_picture',
        ),
    ]
