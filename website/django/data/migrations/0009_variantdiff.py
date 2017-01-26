# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-26 14:53
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_datarelease_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='VariantDiff',
            fields=[
                ('variant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='data.Variant')),
                ('diff', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
