# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssf', '0015_auto_20171001_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='contribution',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
