# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-15 08:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openra', '0003_auto_20160314_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('posted', models.DateTimeField(default=datetime.datetime.now, verbose_name='dated added')),
            ],
            options={
                'verbose_name_plural': 'MapCategories',
            },
        ),
        migrations.AddField(
            model_name='maps',
            name='categories',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='maps',
            name='description',
            field=models.CharField(blank=True, max_length=4000, null=True),
        ),
        migrations.AlterField(
            model_name='maps',
            name='map_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
