# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 17:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='timeentry',
            options={'verbose_name_plural': 'Time entries'},
        ),
        migrations.AlterField(
            model_name='objective',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='timeentry',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='timeentry',
            name='effort',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
