# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,loader
from django.http import HttpResponse
from django.core.mail import send_mail
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
	send_mail('Important major project shashidhar meeting','come at 12 o clock near sbi gate','sharath.12sr@gmail.com',['ppaswanth3@gmail.com','sharath.12sr@gmail.com','ameen.sf@gmail.com'],fail_silently=False)
	print "sent mail nigga"
	return HttpResponse(template.render(context, request))



