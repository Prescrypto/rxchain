# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 23:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0009_prescription_previous_hash'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='previous_hash',
            field=models.CharField(blank=True, default=b'', max_length=255),
        ),
    ]
