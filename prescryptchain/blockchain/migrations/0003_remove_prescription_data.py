# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-09 03:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0002_auto_20170708_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='data',
        ),
    ]
