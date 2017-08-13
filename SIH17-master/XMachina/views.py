from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import login as auth_login 
from django.conf import settings
import googlemaps
from main.models import *
from django.views.decorators.csrf import csrf_exempt
from django.template import *
from django.http import *
import csv
import codecs
import os
import time
# Create your views here.




def mapdataView(request):
	#if request.POST:
		#location=request['coordinates']
		location=(-33.86746, 151.207090)
		gmaps=googlemaps.Client('AIzaSyB4hFa1SMoiUw7Mm7yTGdKGtPxi42mIev4')
		results=gmaps.places_radar(location,1000,type='hospital')['results']
		results+=gmaps.places_radar(location,1000,type='school')['results']

		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename="data.csv"'
		writer = csv.writer(response)
		for i in results:
			k=i['geometry']['location']
			writer.writerow([k['lat'],k['lng']])
		return response

@csrf_exempt
def sendview(request):
	if request.POST:
		test=Test(test=1)
		test.save()
		return HttpResponse('YOLO')
	return HttpResponse("Say something")

@csrf_exempt
def heatmapsView(request):
	return render_to_response('heatmap.html',)

@csrf_exempt
def hornlogView(request):
	if request.POST:
		hornlog=HornLog()
		hornlog.hornlog=request.body
		hornlog.save()
		return HttpResponse("Success")
	return HttpResponse("No")


@csrf_exempt
def registrationView(request):
	if request.POST:
		device=Device()
		device.deviceID=request.POST['deviceID']
		device.regNum=request.POST['regNum']
		device.UID=request.POST['UID']
		device.save()
		print device
		return HttpResponse("")
	return render_to_response('registration.html')

@csrf_exempt
def loginView(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/agentmain/')
	if request.POST:
			data=request.POST
			username = data['username']
			password = data['password']
			user = auth.authenticate(username=username, password=password)
				
			if user is not None:
				if user.is_active:
					auth_login(request,user)
					return HttpResponseRedirect('/agentmain/')
	else:
			return render_to_response('login.html')


@login_required
def agentmainView(request):
	return	render_to_response('agentmain.html')


def mainView(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/agentmain/')
	return render_to_response('main.html')


