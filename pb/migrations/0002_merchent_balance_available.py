# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchent',
            name='balance_available',
            field=models.IntegerField(default=0),
        ),
    ]
