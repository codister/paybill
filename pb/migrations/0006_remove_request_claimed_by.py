# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pb', '0005_auto_20151013_2328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='claimed_by',
        ),
    ]
