# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-08 01:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180708_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]