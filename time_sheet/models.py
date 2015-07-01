# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Shift(models.Model):
  start = models.TimeField()
  finish = models.TimeField()
  #def __unicode__(self):
      #return self.start

class Duty(models.Model):
  date = models.DateField()
  name = models.CharField(max_length=200)
  summary = models.CharField(max_length=200)
  def __unicode__(self):
      return self.name
