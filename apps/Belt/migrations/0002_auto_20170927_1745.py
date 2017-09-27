# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-27 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Belt', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trips',
            old_name='new_trip',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='trips',
            name='travel_date_from',
            field=models.DateField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
    ]
