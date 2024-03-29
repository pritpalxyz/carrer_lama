# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *




class allInterviews(admin.ModelAdmin):
    list_display = ('submittedBy', 'company','job_title_designation','submittedDate')
    search_fields = ['job_title_designation']
    date_hierarchy = 'submittedDate'
    exclude = ['helpful_count']




admin.site.register(all_colleges)
admin.site.register(qualifications)
admin.site.register(company_interviews,allInterviews)
admin.site.register(socialMediaLinks)