# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-04 07:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wins',
            name='rate',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='wins',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 4, 10, 59, 19, 854000)),
        ),
    ]
