# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-18 11:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('log_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user_name', models.CharField(blank=True, max_length=128, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('amount_added', models.IntegerField(blank=True, null=True)),
                ('amount_withdrawn', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('phone', models.CharField(blank=True, max_length=128, null=True)),
                ('email', models.CharField(blank=True, max_length=128, null=True)),
                ('username', models.CharField(blank=True, max_length=128, null=True)),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
                ('joined_on', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('personal_amount', models.IntegerField(blank=True, null=True)),
                ('amount_taken', models.IntegerField(blank=True, null=True)),
                ('group_contribution', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('wallet_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('wallet_name', models.CharField(blank=True, max_length=128, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, default=None, null=True)),
                ('created_on', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='wallet_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wallet_code', to='wallet.Wallet'),
        ),
        migrations.AddField(
            model_name='logs',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='wallet.User'),
        ),
        migrations.AddField(
            model_name='logs',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wallet', to='wallet.Wallet'),
        ),
    ]
