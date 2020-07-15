# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2020-04-03 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0049_add_vr_id_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='Allele_count_exome_EAS_JPN_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_exome_EAS_KOR_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_exome_EAS_OEA_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_exome_NFE_BGR_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_exome_NFE_EST_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_exome_NFE_NWE_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_exome_NFE_ONF_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_exome_NFE_SEU_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_exome_NFE_SWE_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_genome_EAS_JPN_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_genome_EAS_KOR_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_genome_EAS_OEA_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_genome_NFE_BGR_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_genome_NFE_EST_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_genome_NFE_NWE_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_genome_NFE_ONF_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_genome_NFE_SEU_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_genome_NFE_SWE_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_hom_exome_EAS_JPN_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_hom_exome_EAS_KOR_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_hom_exome_EAS_OEA_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_hom_exome_NFE_BGR_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_hom_exome_NFE_EST_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_hom_exome_NFE_NWE_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_hom_exome_NFE_ONF_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_hom_exome_NFE_SEU_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_hom_exome_NFE_SWE_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_hom_genome_EAS_JPN_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_hom_genome_EAS_KOR_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_hom_genome_EAS_OEA_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_hom_genome_NFE_BGR_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_hom_genome_NFE_EST_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_hom_genome_NFE_NWE_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_hom_genome_NFE_ONF_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_hom_genome_NFE_SEU_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_count_hom_genome_NFE_SWE_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_frequency_exome_EAS_JPN_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_frequency_exome_EAS_KOR_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_frequency_exome_EAS_OEA_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_frequency_exome_NFE_BGR_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_frequency_exome_NFE_EST_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_frequency_exome_NFE_NWE_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_frequency_exome_NFE_ONF_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_frequency_exome_NFE_SEU_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_frequency_exome_NFE_SWE_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_frequency_genome_EAS_JPN_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_frequency_genome_EAS_KOR_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_frequency_genome_EAS_OEA_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_frequency_genome_NFE_BGR_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_frequency_genome_NFE_EST_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_frequency_genome_NFE_NWE_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_frequency_genome_NFE_ONF_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_frequency_genome_NFE_SEU_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_frequency_genome_NFE_SWE_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_number_exome_EAS_JPN_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_number_exome_EAS_KOR_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_number_exome_EAS_OEA_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_number_exome_NFE_BGR_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_number_exome_NFE_EST_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_number_exome_NFE_NWE_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_number_exome_NFE_ONF_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_number_exome_NFE_SEU_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_number_exome_NFE_SWE_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_number_genome_EAS_JPN_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_number_genome_EAS_KOR_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_number_genome_EAS_OEA_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_number_genome_NFE_BGR_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_number_genome_NFE_EST_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_number_genome_NFE_NWE_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_number_genome_NFE_ONF_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_number_genome_NFE_SEU_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Allele_number_genome_NFE_SWE_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='faf95_popmax_exome_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='faf95_popmax_genome_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='faf95_popmax_population_exome_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='faf95_popmax_population_genome_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_exome_EAS_JPN_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_exome_EAS_KOR_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_exome_EAS_OEA_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_exome_NFE_BGR_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_exome_NFE_EST_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_exome_NFE_NWE_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_exome_NFE_ONF_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_exome_NFE_SEU_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_exome_NFE_SWE_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_genome_EAS_JPN_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_genome_EAS_KOR_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_genome_EAS_OEA_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_genome_NFE_BGR_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_genome_NFE_EST_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_genome_NFE_NWE_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_genome_NFE_ONF_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_genome_NFE_SEU_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_genome_NFE_SWE_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_hom_exome_EAS_JPN_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_hom_exome_EAS_KOR_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_hom_exome_EAS_OEA_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_hom_exome_NFE_BGR_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_hom_exome_NFE_EST_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_hom_exome_NFE_NWE_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_hom_exome_NFE_ONF_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_hom_exome_NFE_SEU_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_hom_exome_NFE_SWE_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_hom_genome_EAS_JPN_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_hom_genome_EAS_KOR_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_hom_genome_EAS_OEA_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_hom_genome_NFE_BGR_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_hom_genome_NFE_EST_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_hom_genome_NFE_NWE_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_hom_genome_NFE_ONF_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_hom_genome_NFE_SEU_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_count_hom_genome_NFE_SWE_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_frequency_exome_EAS_JPN_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_frequency_exome_EAS_KOR_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_frequency_exome_EAS_OEA_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_frequency_exome_NFE_BGR_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_frequency_exome_NFE_EST_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_frequency_exome_NFE_NWE_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_frequency_exome_NFE_ONF_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_frequency_exome_NFE_SEU_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_frequency_exome_NFE_SWE_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_frequency_genome_EAS_JPN_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_frequency_genome_EAS_KOR_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_frequency_genome_EAS_OEA_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_frequency_genome_NFE_BGR_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_frequency_genome_NFE_EST_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_frequency_genome_NFE_NWE_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_frequency_genome_NFE_ONF_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_frequency_genome_NFE_SEU_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_frequency_genome_NFE_SWE_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_number_exome_EAS_JPN_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_number_exome_EAS_KOR_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_number_exome_EAS_OEA_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_number_exome_NFE_BGR_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_number_exome_NFE_EST_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_number_exome_NFE_NWE_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_number_exome_NFE_ONF_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_number_exome_NFE_SEU_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_number_exome_NFE_SWE_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_number_genome_EAS_JPN_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_number_genome_EAS_KOR_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_number_genome_EAS_OEA_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_number_genome_NFE_BGR_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_number_genome_NFE_EST_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_number_genome_NFE_NWE_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_number_genome_NFE_ONF_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_number_genome_NFE_SEU_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Allele_number_genome_NFE_SWE_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='faf95_popmax_exome_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='faf95_popmax_genome_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='faf95_popmax_population_exome_GnomAD',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='faf95_popmax_population_genome_GnomAD',
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