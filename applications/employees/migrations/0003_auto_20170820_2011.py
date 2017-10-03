# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-20 20:11
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('employees', '0002_auto_20170820_0423'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProxyGroup',
            fields=[
            ],
            options={
                'verbose_name': 'група',
                'verbose_name_plural': 'групи',
                'indexes': [],
                'proxy': True,
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='middle_name',
            field=models.CharField(max_length=64, verbose_name='по батькові'),
        ),
        migrations.AlterUniqueTogether(
            name='deptemp',
            unique_together=set([('employee', 'department')]),
        ),
    ]
