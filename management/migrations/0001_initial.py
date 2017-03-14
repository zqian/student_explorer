# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-13 20:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Cohort',
            fields=[
                ('code', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('group', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='StudentAdvisorCohort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Advisor')),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Cohort')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Student')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='studentadvisorcohort',
            unique_together=set([('student', 'cohort', 'advisor')]),
        ),
    ]
