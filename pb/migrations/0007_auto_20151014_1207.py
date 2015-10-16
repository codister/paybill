# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pb', '0006_remove_request_claimed_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='btc_amount',
            field=models.DecimalField(default=0.0, max_digits=20, decimal_places=0),
        ),
    ]
