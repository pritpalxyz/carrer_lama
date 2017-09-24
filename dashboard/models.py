# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from home.models import *
from django.conf import settings
import random, os,string, uuid
# Create your models here.


# Create your models here.
def get_a_to_z_upload_path(sub_folder, filename):
	ext = filename.split(".").pop()
	folder = random.choice(string.ascii_lowercase)
	name = '%s_%s' % (folder, uuid.uuid4().hex)
	folder_path = os.path.join(settings.MEDIA_SUB_FOLDER_NAME, sub_folder, folder)
	folder_root = os.path.join(settings.MEDIA_ROOT, folder_path)
	if not os.path.exists(folder_root):
		os.makedirs(folder_root)
	return os.path.join(folder_path, '%s.%s' % (name, ext))


def get_profile_image(instance,filename):
	return get_a_to_z_upload_path('profile_image',filename)

class userinformation(models.Model):
	user                = models.OneToOneField(User)
	userProfileImage    = models.ImageField(upload_to=get_profile_image,default='https://eliaslealblog.files.wordpress.com/2014/03/user-200.png')
	current_job_profile     = models.CharField(max_length=500,default='')
	current_location        = models.CharField(max_length=500,default='')


	def __str__(self):
		return self.user.username

class interviews(models.Model):

	ANYONMOUS_STAT          = (
		('1','1'),
		('0','0'),
	)
	HOW_FIND_STAT           = (
		('easy','easy'),
		('difficult','difficult'),
		('very_difficult','very_difficult'),
	)
	OFFER_START_STAT        = (
		('yes','yes'),
		('no','no'),
		('awaiting','awaiting'),
	)

	SHOW_STAT               = (
		('1','1'),
		('0','0')
	)
	submittedBy             = models.ForeignKey(User)
	company                 = models.ForeignKey(companies)
	designation             = models.CharField(max_length=1000,default='')
	yearOfExperience        = models.CharField(max_length=1000,default='')
	highestQualification    = models.CharField(max_length=1000,default='')
	anyonmousStat           = models.CharField(max_length=50,choices=ANYONMOUS_STAT,default='0')
	processOfInterview      = models.TextField(default='')
	month                   = models.CharField(max_length=200,default='')
	year                    = models.CharField(max_length=200,default='')
	source                  = models.CharField(max_length=500,default='')
	howfind                 = models.CharField(max_length=100,choices=HOW_FIND_STAT,default='easy')
	getOfferstat            = models.CharField(max_length=100,choices=OFFER_START_STAT,default='yes')
	otherComment            = models.TextField(default='')
	showStat                = models.CharField(max_length=50,default='0',choices=SHOW_STAT)
	submittedDate 			= models.DateField(null=True,auto_now_add=True)


	def __str__(self):
		return self.company.company_name + " | " + self.designation


class questionsAsked(models.Model):
	interview           = models.ForeignKey(interviews)
	questions           = models.TextField()


