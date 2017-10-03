# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-21 01:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_auto_20170820_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='signed_on_notifications',
            field=models.BooleanField(default=True, verbose_name='Підписаний на сповіщення'),
        ),
        migrations.AlterUniqueTogether(
            name='deptemp',
            unique_together=set([('employee', 'department')]),
        ),
    ]
