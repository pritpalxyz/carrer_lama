# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20171012_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_interviews',
            name='apear_year',
            field=models.CharField(choices=[('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018')], max_length=100, verbose_name='Which year did you appear for the process?'),
        ),
    ]
