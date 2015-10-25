# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pb', '0002_merchent_balance_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='payment_status',
        ),
        migrations.AddField(
            model_name='payment',
            name='ispaid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='payment',
            name='error_message',
            field=models.TextField(default='None'),
        ),
    ]
