# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pb', '0007_auto_20151014_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='btc_amount',
            field=models.FloatField(default=0),
        ),
    ]
