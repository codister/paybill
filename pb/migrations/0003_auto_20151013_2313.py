# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pb', '0002_auto_20151013_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='claiming_time',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='confirmation_id',
            field=models.CharField(default='Not Yet Provided', max_length=200),
        ),
        migrations.AlterField(
            model_name='request',
            name='timeremaining',
            field=models.TimeField(auto_now=True),
        ),
    ]
