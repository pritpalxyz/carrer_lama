# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from .models import *



admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(country)
admin.site.register(States)
admin.site.register(category)
admin.site.register(designations)
admin.site.register(companies)
admin.site.register(offices)
admin.site.register(Teams)
admin.site.register(reviews)

admin.site.register(contacted)