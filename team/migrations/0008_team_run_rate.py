# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-06 09:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0007_auto_20161106_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='run_rate',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
