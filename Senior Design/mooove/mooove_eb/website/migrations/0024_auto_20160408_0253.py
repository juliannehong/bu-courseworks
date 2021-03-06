# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-08 02:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0023_auto_20160408_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accelerometer',
            name='idanklet',
            field=models.ForeignKey(blank=True, db_column='idAnklet', default=2, on_delete=django.db.models.deletion.CASCADE, to='website.AnkletGeneral'),
        ),
        migrations.AlterField(
            model_name='accelerometer',
            name='idcow',
            field=models.ForeignKey(blank=True, db_column='idCow', default=6, on_delete=django.db.models.deletion.CASCADE, to='website.CowGeneral'),
        ),
        migrations.AlterField(
            model_name='activitylevel',
            name='idcow',
            field=models.ForeignKey(blank=True, db_column='idCow', default=6, on_delete=django.db.models.deletion.CASCADE, to='website.CowGeneral'),
        ),
        migrations.AlterField(
            model_name='ankletgeneral',
            name='idcow',
            field=models.ForeignKey(blank=True, db_column='idCow', default=6, on_delete=django.db.models.deletion.CASCADE, related_name='cow_anklet', to='website.CowGeneral'),
        ),
        migrations.AlterField(
            model_name='cowculatedlocation',
            name='idanklet',
            field=models.ForeignKey(blank=True, db_column='idAnklet', default=2, on_delete=django.db.models.deletion.CASCADE, to='website.AnkletGeneral'),
        ),
        migrations.AlterField(
            model_name='cowculatedlocation',
            name='idcow',
            field=models.ForeignKey(blank=True, db_column='idCow', default=6, on_delete=django.db.models.deletion.CASCADE, to='website.CowGeneral'),
        ),
        migrations.AlterField(
            model_name='cowgroups',
            name='idcow',
            field=models.ForeignKey(blank=True, db_column='idCow', default=6, on_delete=django.db.models.deletion.CASCADE, to='website.CowGeneral'),
        ),
        migrations.AlterField(
            model_name='friendships',
            name='idcowfriend',
            field=models.ForeignKey(blank=True, db_column='idCowFriend', default=6, on_delete=django.db.models.deletion.CASCADE, related_name='cowfriend', to='website.CowGeneral'),
        ),
        migrations.AlterField(
            model_name='friendships',
            name='idcoworiginal',
            field=models.ForeignKey(blank=True, db_column='idCowOriginal', default=6, on_delete=django.db.models.deletion.CASCADE, related_name='coworiginal', to='website.CowGeneral'),
        ),
        migrations.AlterField(
            model_name='location',
            name='idanklet',
            field=models.ForeignKey(blank=True, db_column='idAnklet', default=2, on_delete=django.db.models.deletion.CASCADE, to='website.AnkletGeneral'),
        ),
        migrations.AlterField(
            model_name='location',
            name='idcow',
            field=models.ForeignKey(blank=True, db_column='idCow', default=6, on_delete=django.db.models.deletion.CASCADE, to='website.CowGeneral'),
        ),
        migrations.AlterField(
            model_name='microphone',
            name='idanklet',
            field=models.ForeignKey(blank=True, db_column='idAnklet', default=2, on_delete=django.db.models.deletion.CASCADE, to='website.AnkletGeneral'),
        ),
        migrations.AlterField(
            model_name='microphone',
            name='idcow',
            field=models.ForeignKey(blank=True, db_column='idCow', default=6, on_delete=django.db.models.deletion.CASCADE, to='website.CowGeneral'),
        ),
        migrations.AlterField(
            model_name='pulse',
            name='idanklet',
            field=models.ForeignKey(blank=True, db_column='idAnklet', default=2, on_delete=django.db.models.deletion.CASCADE, to='website.AnkletGeneral'),
        ),
        migrations.AlterField(
            model_name='pulse',
            name='idcow',
            field=models.ForeignKey(blank=True, db_column='idCow', default=6, on_delete=django.db.models.deletion.CASCADE, to='website.CowGeneral'),
        ),
        migrations.AlterField(
            model_name='sociallevel',
            name='idcow',
            field=models.ForeignKey(blank=True, db_column='idCow', default=6, on_delete=django.db.models.deletion.CASCADE, to='website.CowGeneral'),
        ),
        migrations.AlterField(
            model_name='stepcount',
            name='idcow',
            field=models.ForeignKey(blank=True, db_column='idCow', default=6, on_delete=django.db.models.deletion.CASCADE, to='website.CowGeneral'),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='idcow',
            field=models.ForeignKey(blank=True, db_column='idCow', default=6, on_delete=django.db.models.deletion.CASCADE, related_name='cow_temperature', to='website.CowGeneral'),
        ),
    ]
