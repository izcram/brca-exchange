# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-10-05 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0023_add_dbid_lovd'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='Review_Status_ClinVar',
            field=models.TextField(default=b'-'),
        ),
        migrations.AddField(
            model_name='report',
            name='Summary_Evidence_ClinVar',
            field=models.TextField(default=b'-'),
        ),
    ]