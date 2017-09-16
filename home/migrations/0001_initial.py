# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 05:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='companies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=1000)),
                ('comapny_logo', models.ImageField(upload_to=home.models.get_company_image)),
                ('weburl', models.TextField(default='')),
                ('startedDate', models.DateField()),
                ('ratings', models.CharField(help_text='This Value will change basis on user reviews', max_length=100)),
                ('company_description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
        migrations.CreateModel(
            name='country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='designations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation_name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='offices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office_title', models.CharField(max_length=800)),
                ('office_address', models.TextField()),
                ('office_contact', models.CharField(max_length=500)),
                ('office_latitude', models.CharField(max_length=50)),
                ('office_longitude', models.CharField(max_length=50)),
                ('companyid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.companies')),
            ],
        ),
        migrations.CreateModel(
            name='reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_or_title', models.CharField(max_length=1000)),
                ('dateposted', models.DateField(auto_now_add=True, null=True)),
                ('slug_url', models.CharField(max_length=2000)),
                ('skill_development_learning', models.CharField(choices=[('1.0', '1.0'), ('1.5', '1.5'), ('2.0', '2.0'), ('2.5', '2.5'), ('3.0', '3.0'), ('3.5', '3.5'), ('4.0', '4.0'), ('4.5', '4.5'), ('5.0', '5.0')], max_length=50, verbose_name='Skill development/learning')),
                ('work_life_balance', models.CharField(choices=[('1.0', '1.0'), ('1.5', '1.5'), ('2.0', '2.0'), ('2.5', '2.5'), ('3.0', '3.0'), ('3.5', '3.5'), ('4.0', '4.0'), ('4.5', '4.5'), ('5.0', '5.0')], max_length=50, verbose_name='Work-Life balance')),
                ('compensation_benifits', models.CharField(choices=[('1.0', '1.0'), ('1.5', '1.5'), ('2.0', '2.0'), ('2.5', '2.5'), ('3.0', '3.0'), ('3.5', '3.5'), ('4.0', '4.0'), ('4.5', '4.5'), ('5.0', '5.0')], max_length=50, verbose_name='Compensation & Benefits')),
                ('company_culture', models.CharField(choices=[('1.0', '1.0'), ('1.5', '1.5'), ('2.0', '2.0'), ('2.5', '2.5'), ('3.0', '3.0'), ('3.5', '3.5'), ('4.0', '4.0'), ('4.5', '4.5'), ('5.0', '5.0')], max_length=50, verbose_name='Company culture')),
                ('job_security', models.CharField(choices=[('1.0', '1.0'), ('1.5', '1.5'), ('2.0', '2.0'), ('2.5', '2.5'), ('3.0', '3.0'), ('3.5', '3.5'), ('4.0', '4.0'), ('4.5', '4.5'), ('5.0', '5.0')], max_length=50, verbose_name='Job Security')),
                ('career_griwth_oppur', models.CharField(choices=[('1.0', '1.0'), ('1.5', '1.5'), ('2.0', '2.0'), ('2.5', '2.5'), ('3.0', '3.0'), ('3.5', '3.5'), ('4.0', '4.0'), ('4.5', '4.5'), ('5.0', '5.0')], max_length=50, verbose_name='Career growth & opportunities')),
                ('work_statisfaction', models.CharField(choices=[('1.0', '1.0'), ('1.5', '1.5'), ('2.0', '2.0'), ('2.5', '2.5'), ('3.0', '3.0'), ('3.5', '3.5'), ('4.0', '4.0'), ('4.5', '4.5'), ('5.0', '5.0')], max_length=50, verbose_name='Work Satisfaction')),
                ('working_days', models.CharField(choices=[('Monday to Saturday', 'Monday to Saturday'), ('Monday to Friday', 'Monday to Friday'), ('Monday to Sunday', 'Monday to Sunday')], max_length=200, verbose_name='Working Days')),
                ('job_travel', models.TextField()),
                ('working_time', models.CharField(choices=[('Normal', 'Normal'), ('Strict', 'Strict'), ('Flexible', 'Flexible')], max_length=100)),
                ('working_starttime', models.TimeField()),
                ('working_endtime', models.TimeField()),
                ('likes', models.TextField()),
                ('dislikes', models.TextField()),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.designations')),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=1000)),
                ('countryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.country')),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_member_name', models.CharField(max_length=500)),
                ('team_member_image', models.ImageField(upload_to=home.models.get_profile_image)),
                ('position', models.CharField(choices=[('Current', 'Current'), ('Past', 'Past')], max_length=200)),
                ('education', models.TextField()),
                ('companyid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.companies')),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.designations')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.States')),
            ],
        ),
        migrations.AddField(
            model_name='companies',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.States'),
        ),
    ]
