# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pb', '0004_auto_20151013_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='claimed_by',
            field=models.ForeignKey(to='pb.Merchent'),
        ),
    ]
