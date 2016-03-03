# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-03 16:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side', models.CharField(choices=[(0, 'dark'), (1, 'light')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Wins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2016, 3, 3, 19, 13, 16, 459000))),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Team')),
            ],
        ),
    ]
