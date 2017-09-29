# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 23:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ssf', '0007_auto_20170929_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='senateseedfund',
            name='amount_given',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='senateseedfund',
            name='contributers',
            field=models.ManyToManyField(blank=True, related_name='contributers', to=settings.AUTH_USER_MODEL),
        ),
    ]
