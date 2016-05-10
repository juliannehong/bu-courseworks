# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 04:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fitbit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cow_name', models.CharField(max_length=20)),
                ('cow_age', models.IntegerField()),
                ('device_id', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='member',
            name='product_id',
        ),
    ]
