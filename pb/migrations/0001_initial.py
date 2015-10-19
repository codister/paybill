# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('bill_type', models.CharField(max_length=128)),
                ('country', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Merchent',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('contact_num', models.CharField(max_length=128)),
                ('landline_num', models.CharField(max_length=128)),
                ('cnic_photo', models.ImageField(blank=True, upload_to='cnic_images')),
                ('cinc_selfi_photo', models.ImageField(blank=True, upload_to='cnic_selfi_images')),
                ('isverified_email', models.BooleanField(default=False)),
                ('is_account_active', models.BooleanField(default=False)),
                ('is_admin_approve', models.BooleanField(default=False)),
                ('is_admin_blocked', models.BooleanField(default=False)),
                ('billing_id_number', models.CharField(max_length=128)),
                ('total_earnings', models.DecimalField(max_digits=20, default=0.0, decimal_places=15)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('payment_status', models.CharField(max_length=128)),
                ('payment_amount', models.IntegerField(default=0)),
                ('payment_method', models.CharField(max_length=128)),
                ('error_message', models.TextField(default='Payment Authorized No Error Messages')),
                ('merchent', models.ForeignKey(to='pb.Merchent')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('bill_type', models.CharField(max_length=128)),
                ('billing_company', models.CharField(max_length=128)),
                ('payment_method', models.CharField(default='BTC', max_length=128)),
                ('country', models.CharField(default='Pakistan', max_length=128)),
                ('pkr_bill_amount', models.IntegerField(default=0)),
                ('contact_num', models.CharField(max_length=128)),
                ('bill_id_num', models.CharField(max_length=128)),
                ('is_paid', models.BooleanField(default=False)),
                ('is_completed', models.BooleanField(default=False)),
                ('isclaimed', models.BooleanField(default=False)),
                ('timeremaining', models.TimeField(auto_now=True)),
                ('issue_message', models.TextField(default='No Error or Issue all Clear ')),
                ('confirmation_id', models.CharField(default='Not Yet Provided', max_length=200)),
                ('btc_confirmations', models.IntegerField(default=0)),
                ('btc_address', models.CharField(max_length=400)),
                ('btc_amount', models.FloatField(default=0)),
                ('claiming_time', models.TimeField(auto_now=True)),
                ('email_address', models.CharField(blank=True, max_length=100)),
                ('payment_completed', models.BooleanField(default=False)),
                ('request_token', models.BooleanField(default=True)),
                ('time_claimed_on', models.DateTimeField(blank=True)),
            ],
        ),
    ]
