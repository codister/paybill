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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('bill_type', models.CharField(max_length=128)),
                ('country', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Merchent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('contact_num', models.CharField(max_length=128)),
                ('landline_num', models.CharField(max_length=128)),
                ('cnic_photo', models.ImageField(upload_to='cnic_images', blank=True)),
                ('cinc_selfi_photo', models.ImageField(upload_to='cnic_selfi_images', blank=True)),
                ('isverified_email', models.BooleanField(default=False)),
                ('is_account_active', models.BooleanField(default=False)),
                ('is_admin_approve', models.BooleanField(default=False)),
                ('is_admin_blocked', models.BooleanField(default=False)),
                ('billing_id_number', models.CharField(max_length=128)),
                ('total_earnings', models.IntegerField(default=0)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
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
                ('issue_message', models.TextField(default='No Error or Issue all Clear ')),
                ('confirmation_txid', models.CharField(default='No Information ID Provided', max_length=128)),
                ('btc_confirmations', models.IntegerField(default=0)),
                ('btc_address', models.CharField(max_length=400)),
                ('btc_amount', models.FloatField(default=0)),
                ('email_address', models.CharField(max_length=100, blank=True)),
                ('payment_completed', models.BooleanField(default=False)),
                ('request_token', models.BooleanField(default=True)),
                ('time_claimed_on', models.DateTimeField(blank=True)),
                ('claimer', models.ForeignKey(default='1', to='pb.Merchent')),
            ],
        ),
    ]
