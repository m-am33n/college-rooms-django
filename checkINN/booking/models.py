# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class College(models.Model):
	college_id = models.IntegerField(primary_key=True)
	college_name = models.CharField(max_length=200)
	college_loc = models.CharField(max_length=200)
	avail_sdate = models.DateTimeField()
	avail_edate = models.DateTimeField()
	college_price = models.IntegerField(default=100)
	availability = models.BooleanField(default=True)

	def __unicode__(self):
		return u'%s' % (self.college_name)