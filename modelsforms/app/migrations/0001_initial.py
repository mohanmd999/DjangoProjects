# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-16 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=220)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
