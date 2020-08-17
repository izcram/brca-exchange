# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2020-07-06 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0051_add_ca_id_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='Case_control_LR_exLOVD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Pathology_LR_exLOVD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Case_control_LR_exLOVD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Pathology_LR_exLOVD',
            field=models.TextField(null=True),
        ),
        migrations.RunSQL(
            """
            DROP MATERIALIZED VIEW IF EXISTS currentvariant;
            CREATE MATERIALIZED VIEW currentvariant AS (
                SELECT * FROM "variant" WHERE (
                    "id" IN ( SELECT DISTINCT ON ("Genomic_Coordinate_hg38") "id" FROM "variant" ORDER BY "Genomic_Coordinate_hg38" ASC, "Data_Release_id" DESC )
                )
            );
            """
        ),
    ]
