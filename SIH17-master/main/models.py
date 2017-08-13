from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Test(models.Model):
	test=models.IntegerField(default=0)

class Agent(models.Model):
	username=models.CharField(max_length=10,default="")
	password=models.CharField(max_length=10,default="")
	def __unicode__(self):
		return self.username
class Device(models.Model):
	deviceID=models.CharField(max_length=10,default='')
	regNum=models.CharField(max_length=10,default='')
	UID=models.CharField(max_length=12,default='')
	def __unicode__(self):
		return self.deviceID

class HornLog(models.Model):
	#device=models.ForeignKey(Device)
	hornlog=models.CharField(max_length=50,default='')
	def __unicode__(self):
		return self.hornlog

class SensitivePoint(models.Model):
	location_x=models.CharField(max_length=20,default='')
	location_y=models.CharField(max_length=20,default='')
	def __unicode__(self):
		return self.location_x+","+self.location_y

class Indices(models.Model):
	location_x=models.CharField(max_length=20,default='')
	location_y=models.CharField(max_length=20,default='')
	def __unicode__(self):
		return self.location_x+","+self.location_y






