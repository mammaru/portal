#!coding:utf-8
from django.conf.urls import patterns, url
from time_sheet import views

urlpatterns = patterns('',
        url(r'^$', views.show, name='show'),
        url(r'^edit/$', views.edit, name='edit'),
)
