# -*- coding: utf-8 -*-
from django import forms
from time_sheet.models import Shift

# Create your forms here.

class ShiftForm(forms.ModelForm):
    '''シフトのフォーム'''
    #start = forms.TimeField()
    #finish = forms.TimeField()
    class Meta:
        model = Shift
        fields = ('start', 'finish',)
