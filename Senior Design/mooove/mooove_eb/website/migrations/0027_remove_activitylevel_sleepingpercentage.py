# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-16 23:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_auto_20160415_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activitylevel',
            name='sleepingpercentage',
        ),
    ]
