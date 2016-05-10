# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-12 17:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0010_auto_20160305_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='fitbit',
            name='noise',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='fitbit',
            name='temperature',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='fitbit',
            name='user',
            field=models.ForeignKey(default='mooove', on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL),
        ),
    ]