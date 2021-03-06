# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 12:00
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gprojects', '0037_auto_20160401_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='gtask_link',
            name='gbaseline',
            field=models.ForeignKey(blank=True, default=15, null=True, on_delete=django.db.models.deletion.CASCADE, to='gprojects.Gbaseline'),
        ),
        migrations.AlterField(
            model_name='gtask',
            name='progress',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='Progress'),
        ),
    ]
