#!coding:utf-8
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import RequestContext
from time_sheet.models import Shift
from time_sheet.forms import ShiftForm

# Create your views here.
def shift_list(request):
    #return HttpResponse('勤務表表示')
    shifts = Shift.objects.all()
    return render_to_response('time_sheet/shift_list.html', {'shifts': shifts}, context_instance=RequestContext(request))

def shift_edit(request, shift_id=None):
    '''シフトの編集'''
    #return HttpResponse(u'書籍の編集')
    if shift_id:   # shift_id が指定されている (修正時)
        shift = get_object_or_404(Shift, pk=shift_id)
    else:         # shift_id が指定されていない (追加時)
        shift= Shift()

    if request.method == 'POST':
        form = ShiftForm(request.POST, instance=shift)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            shift = form.save(commit=False)
            shift.save()
            return redirect('time_sheet:shift_list')
    else:    # GET の時
        form = ShiftForm(instance=shift)  # shift インスタンスからフォームを作成

    return render_to_response('time_sheet/shift_edit.html',
                              dict(form=form, shift_id=shift_id),
                              context_instance=RequestContext(request))

def shift_delete(request, shift_id):
    '''シフトの削除'''
    #return HttpResponse(u'書籍の削除')
    shift = get_object_or_404(Shift, pk=shift_id)
    shift.delete()
    return redirect('time_sheet:shift_list')
