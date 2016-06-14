# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 05:07
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wolf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('excerpt', models.TextField(blank=True)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now)),
                ('slug', models.SlugField(unique_for_date='pub_date')),
                ('enable_comments', models.BooleanField(default=True)),
                ('featured', models.BooleanField(default=False)),
                ('status', models.IntegerField(choices=[(1, 'Live'), (2, 'Draft'), (3, 'Hidden')], default=1)),
                ('tags', tagging.fields.TagField(blank=True, default=b'', help_text='Separate tags with spaces.', max_length=255)),
                ('excerpt_html', models.TextField(blank=True, editable=False)),
                ('body_html', models.TextField(blank=True, editable=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pub_date'],
                'verbose_name_plural': 'Entries',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(help_text='Suggested value automatically generated from title. Must be unique.', unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(help_text='Maximum 250 characters.', max_length=250),
        ),
        migrations.AddField(
            model_name='entry',
            name='categories',
            field=models.ManyToManyField(to='wolf.Category'),
        ),
    ]