# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-30 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apl', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='number',
        ),
        migrations.AddField(
            model_name='customer',
            name='addr',
            field=models.CharField(default=1, max_length=220),
            preserve_default=False,
        ),
    ]
