# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 05:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wolf', '0002_auto_20160613_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='tags',
        ),
    ]
