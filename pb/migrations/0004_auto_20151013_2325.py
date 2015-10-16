# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pb', '0003_auto_20151013_2313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='request_type',
            new_name='bill_type',
        ),
        migrations.AlterField(
            model_name='request',
            name='claimed_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
