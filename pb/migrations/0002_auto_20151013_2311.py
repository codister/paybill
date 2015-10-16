# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='country',
            field=models.CharField(default='Pakistan', max_length=128),
        ),
    ]
