# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-01 09:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
        ('matches', '0010_matches_away'),
    ]

    operations = [
        migrations.AddField(
            model_name='matches',
            name='result',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='match_result', to='team.Team'),
            preserve_default=False,
        ),
    ]
