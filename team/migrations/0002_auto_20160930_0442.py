# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 23:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='player_image',
            field=models.FileField(upload_to=''),
        ),
    ]
