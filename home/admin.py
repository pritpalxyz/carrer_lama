# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from .models import *



admin.site.unregister(Group)
# admin.site.unregister(User)


class allCompaniesShow(admin.ModelAdmin):
    list_display = ('company_name', 'state','startedDate')
    search_fields = ['company_name']




admin.site.register(country)
admin.site.register(States)
admin.site.register(category)
admin.site.register(designations)
admin.site.register(companies,allCompaniesShow)

