# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 20:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20171012_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_interviews',
            name='highest_qualification',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.qualifications', verbose_name='What is the highest qualification at the time of interview?'),
        ),
    ]
