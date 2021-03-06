# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-02 18:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seumich', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(['ALTER TABLE `"CNLYR002"."BG_STDNT_ADVSR_ROLE"` DROP PRIMARY KEY, ADD PRIMARY KEY (`STDNT_KEY`, `ADVSR_KEY`, `ADVSR_ROLE_KEY`);']),
        migrations.RunSQL(['ALTER TABLE `"CNLYR002"."BG_STDNT_CHRT_MNTR"` DROP PRIMARY KEY, ADD PRIMARY KEY (`STDNT_KEY`, `MNTR_KEY`, `CHRT_KEY`);']),
        migrations.RunSQL(['ALTER TABLE `"CNLYR002"."FC_STDNT_CLASS_SCR"` DROP PRIMARY KEY, ADD PRIMARY KEY (`STDNT_KEY`, `CLASS_SITE_KEY`);']),
        migrations.RunSQL(['ALTER TABLE `"CNLYR002"."FC_STDNT_CLASS_ASSGN"` DROP PRIMARY KEY, ADD PRIMARY KEY (`STDNT_KEY`, `CLASS_SITE_KEY`, `ASSGN_KEY`);']),
        migrations.RunSQL(['ALTER TABLE `"CNLYR002"."FC_STDNT_CLASS_ACAD_PERF"` DROP PRIMARY KEY, ADD PRIMARY KEY (`STDNT_KEY`, `CLASS_SITE_KEY`, `ACAD_PERF_KEY`);']),
        migrations.RunSQL(['ALTER TABLE `"CNLYR002"."FC_CLASS_WKLY_SCR"` DROP PRIMARY KEY, ADD PRIMARY KEY (`CLASS_SITE_KEY`, `WEEK_END_DT_KEY`);']),
        migrations.RunSQL(['ALTER TABLE `"CNLYR002"."FC_STDNT_CLASS_WKLY_EVENT"` DROP PRIMARY KEY, ADD PRIMARY KEY (`STDNT_KEY`, `CLASS_SITE_KEY`, `WEEK_END_DT_KEY`);']),
        migrations.RunSQL(['ALTER TABLE `"CNLYR002"."FC_STDNT_CLASS_WKLY_SCR"` DROP PRIMARY KEY, ADD PRIMARY KEY (`STDNT_KEY`, `CLASS_SITE_KEY`, `WEEK_END_DT_KEY`);']),
        migrations.RunSQL(['ALTER TABLE `"CNLYR002"."FC_STDNT_CLS_WKLY_ACAD_PRF"` DROP PRIMARY KEY, ADD PRIMARY KEY (`STDNT_KEY`, `CLASS_SITE_KEY`, `WEEK_END_DT_KEY`, `ACAD_PERF_KEY`);']),
    ]
