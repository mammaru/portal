#!coding:utf-8
from django.conf.urls import patterns, url
from time_sheet import views

urlpatterns = patterns('',
        url(r'^shifts/$', views.shift_list, name='shift_list'),
        url(r'^shift/add/$', views.shift_edit, name='shift_add'),
        url(r'^shift/modify/(?P<shift_id>\d+)/$', views.shift_edit, name='shift_modify'),
        url(r'^shift/delete(?P<shift_id>\d+)/$', views.shift_delete, name='shift_delete'),
)
