# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-06 10:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0008_team_run_rate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='run_rate',
            new_name='runrate',
        ),
    ]
