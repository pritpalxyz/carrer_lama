# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_userinformation_alternateuserprofileurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_interviews',
            name='helpful_count',
            field=models.CharField(default='0', max_length=244),
        ),
    ]
