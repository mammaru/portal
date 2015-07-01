# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from time_sheet.models import Shift, Duty

class ShiftAdmin(admin.ModelAdmin):
    list_display = ('id', 'start', 'finish',)
    list_display_links = ('id',)

class DutyAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'name', 'summary',)
    list_display_links = ('id', 'name',)

admin.site.register(Shift, ShiftAdmin)
admin.site.register(Duty, DutyAdmin)
