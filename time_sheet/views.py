#!coding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from time_sheet.models import Shift

# Create your views here.
def show(request):
    #return HttpResponse('勤務表表示')
    shifts = Shift.objects.all()
    return render_to_response('time_sheet/show.html', {'shifts': shifts}, context_instance=RequestContext(request))

def edit(request):
    return HttpResponse('編集')
