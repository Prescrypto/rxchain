# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-28 04:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0015_auto_20180328_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='private_key',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='public_key',
            field=models.TextField(blank=True, default=b''),
        ),
    ]
