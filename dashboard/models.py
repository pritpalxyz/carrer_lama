# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from home.models import *
from django.conf import settings
import random, os,string, uuid
from django.utils.translation import ugettext_lazy as _
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

class all_colleges(models.Model):
	college_name 		= models.TextField(verbose_name='College/University name')

	def __str__(self):
		return self.college_name

	class Meta:
		verbose_name = _("All Colleges/Universities")
		verbose_name_plural = _("All Colleges/Universities")

class qualifications(models.Model):
	qualification_name 	= models.TextField(verbose_name='Quaification')

	def __str__(self):
		return self.qualification_name

	class Meta:
		verbose_name = _("All Qualifications")
		verbose_name_plural = _("All Qualifications")



class company_interviews(models.Model):

	WORK_EXPERIENCE_VAL = (
		('0-1','0-1 years'),
		('1-2','1-2 years'),
		('2-3','2-3 years'),
		('3-4','3-4 years'),
		('4-5','4-5 years'),
		('5-6','5-6 years'),
		('6-7','6-7 years'),
		('7-8','7-8 years'),
		('8-9','8-9 years'),
		('9-10','9-10 years'),
		('10+', '10+ years'),
	)
	KEEP_ANONYMOUS_STAT = (
		('yes','yes'),
		('no','no'),
	)
	MONTHS_STAT 		= (
		('Jan','Jan'),
		('Feb','Feb'),
		('Mar','Mar'),
		('Apr','Apr'),
		('May','May'),
		('Jun','Jun'),
		('Jul','Jul'),
		('Aug','Aug'),
		('Sept','Sept'),
		('Oct','Oct'),
		('Nov','Nov'),
		('Dec','Dec'),
	)

	YEAR_STAT = (
		('2000','2000'),
		('2001','2001'),
		('2002', '2002'),
		('2003', '2003'),
		('2004', '2004'),
		('2005', '2005'),
		('2006', '2006'),
		('2007', '2007'),
		('2008', '2008'),
		('2009', '2009'),
		('2010', '2010'),
		('2011', '2011'),
		('2012', '2012'),
		('2013', '2013'),
		('2014', '2014'),
		('2015', '2015'),
		('2016', '2016'),
		('2017', '2017'),
		('2018', '2018'),

	)


	HOW_GET_STAT 	= (
		('Campus Placement','Campus Placement'),
		('Lateral hiring','Lateral hiring'),
	)
	GET_OFFER_STAT   = (
		('yes','yes'),
		('no','no'),
	)
	SHOW_STAT_VALS = (
		('show','show'),
		('hide','hide'),
	)

	submittedBy 				= models.ForeignKey(User)
	company                 	= models.ForeignKey(companies,verbose_name='Company Name you interviewed for?')
	job_title_designation 		= models.CharField(max_length=1000,default='',verbose_name='Job Title/Designation you interviewed for?')
	college_name 				= models.ForeignKey(all_colleges,verbose_name="What's your college name?",default='')
	work_experience 			= models.CharField(max_length=500,choices=WORK_EXPERIENCE_VAL,verbose_name='Work experience at the time of this interview?',default='')
	keep_anonymous 				= models.CharField(max_length=50,choices=KEEP_ANONYMOUS_STAT,verbose_name='Would you like to keep the post anonymous?',default='')

	#NEXT PAGE FIELDS
	highest_qualification 		= models.ForeignKey(qualifications,verbose_name='What is the highest qualification at the time of interview?',blank=True, null=True)
	apear_month					= models.CharField(max_length=100,choices=MONTHS_STAT,verbose_name='Which month did you appear for the process?',default='')
	apear_year 					= models.CharField(max_length=100,choices=YEAR_STAT,verbose_name='Which year did you appear for the process?',default='')
	interview_prccess 			= models.TextField(verbose_name='Describe the process of interview?',default='')
	anything_else_review 		= models.TextField(verbose_name='Anything else you want to mention about the interview?',default='')
	how_did_you_get 			= models.CharField(max_length=100,choices=HOW_GET_STAT,verbose_name='How did you get the interview?',default='')
	did_you_get_offer 			= models.CharField(max_length=100,choices=GET_OFFER_STAT,verbose_name='Did you get the offer?',default='no')

	show_stat 					= models.CharField(max_length=100,choices=SHOW_STAT_VALS,verbose_name='SHOW/HIDE',default='hide')
	submittedDate = models.DateField(null=True, auto_now_add=True)

	def __str__(self):
		return self.company.company_name + " | " + self.submittedBy.username

	class Meta:
		verbose_name = _("All Interviews")
		verbose_name_plural = _("All Interviews")


# OLD MODEL not in use
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


