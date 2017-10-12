# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 20:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20171012_1853'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='all_colleges',
            options={'verbose_name': 'All Colleges/Universities', 'verbose_name_plural': 'All Colleges/Universities'},
        ),
        migrations.AlterField(
            model_name='company_interviews',
            name='highest_qualification',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='dashboard.qualifications', verbose_name='What is the highest qualification at the time of interview?'),
        ),
    ]
