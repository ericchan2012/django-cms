# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 09:28
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wolf', '0004_entry_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('description_html', models.TextField(blank=True)),
                ('url', models.URLField(unique=True)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now)),
                ('slug', models.SlugField(unique_for_date='pub_date')),
                ('tags', tagging.fields.TagField(blank=True, default=b'', max_length=255)),
                ('enable_comments', models.BooleanField(default=True)),
                ('post_elsewhere', models.BooleanField(default=True, verbose_name='Post to Delicious')),
                ('via_name', models.CharField(blank=True, help_text='The name of the person whose site you spottedthelinkon.Optional.', max_length=250, verbose_name='Via')),
                ('via_url', models.URLField(blank=True, help_text='The URL of the site where you spotted the link.Optional.', verbose_name='Via URL')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
    ]
