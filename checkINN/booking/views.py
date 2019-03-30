# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,loader
from django.http import HttpResponse
# Create your views here.

from .models import College




def index(request):
	context = {}
	template = loader.get_template('booking/index.html')
	return HttpResponse(template.render(context, request))

def view_rooms(request):
	college_list = College.objects.all()
	context = {'college_list': college_list}
	template = loader.get_template('booking/rooms.html')
	return HttpResponse(template.render(context, request))