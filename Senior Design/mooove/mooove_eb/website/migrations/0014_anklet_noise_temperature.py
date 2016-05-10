# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-14 20:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0013_auto_20160312_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anklet',
            fields=[
                ('anklet_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cow_id', models.IntegerField()),
                ('cow_name', models.CharField(blank=True, max_length=500)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anklet', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Noise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noise', models.DecimalField(decimal_places=2, max_digits=5)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('anklet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='noise', to='website.Anklet')),
            ],
        ),
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('anklet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='temperature', to='website.Anklet')),
            ],
        ),
    ]