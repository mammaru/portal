# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from time_sheet.models import Shift, Duty

admin.site.register(Shift)
admin.site.register(Duty)
