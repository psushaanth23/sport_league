# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-06 08:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_auto_20161105_2245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='matches',
        ),
        migrations.RemoveField(
            model_name='team',
            name='points',
        ),
        migrations.RemoveField(
            model_name='team',
            name='rank',
        ),
    ]