# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
import random, os,string, uuid

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


def get_company_image(instance,filename):
	return get_a_to_z_upload_path('companies_image',filename)

def get_profile_image(instance,filename):
	return get_a_to_z_upload_path('team_image',filename)

class country(models.Model):
	country_name    = models.CharField(max_length=1000)

	def __str__(self):
		return self.country_name


class States(models.Model):
	countryid         = models.ForeignKey(country)
	state_name      = models.CharField(max_length=1000)

	def __str__(self):
		return self.state_name + ", " + self.countryid.country_name

class category(models.Model):
	category_name   = models.CharField(max_length=1000)

	def __str__(self):
		return self.category_name


class designations(models.Model):
	designation_name    = models.CharField(max_length=1000)

	def __str__(self):
		return self.designation_name

class companies(models.Model):
	company_name    = models.CharField(max_length=1000)
	comapny_logo    = models.ImageField(upload_to=get_company_image)

	facebook_link 		= models.TextField(default='http://facebook.com')
	google_plus_link 	= models.TextField(default='http://google.com')
	twitter_link 		= models.TextField(default='http://twitter.com')
	linkedin_link 		= models.TextField(default='http://linkedin.com')



	weburl          = models.TextField(default='')
	state           = models.ForeignKey(States)
	startedDate     = models.DateField()
	category        = models.ForeignKey(category)
	ratings         = models.CharField(max_length=100,help_text="This Value will change basis on user reviews")
	company_description = models.TextField()


	def __str__(self):
		return self.company_name


class offices(models.Model):
	companyid           = models.ForeignKey(companies)
	office_title        = models.CharField(max_length=800)
	office_address      = models.TextField()
	office_contact      = models.CharField(max_length=500)
	office_latitude     = models.CharField(max_length=50)
	office_longitude    = models.CharField(max_length=50)


	def __str__(self):
		return self.office_title + " | " + self.companyid.company_name

class Teams(models.Model):
	POSITION_TYPE       =   (
		('Current','Current'),
		('Past','Past'),
	)
	companyid           = models.ForeignKey(companies)
	team_member_name    = models.CharField(max_length=500)
	team_member_image   = models.ImageField(upload_to=get_profile_image)
	designation         = models.ForeignKey(designations)
	position            = models.CharField(max_length=200,choices=POSITION_TYPE)
	education           = models.TextField()
	location            = models.ForeignKey(States)


	def __str__(self):
		return self.team_member_name + " | " + self.companyid.company_name







class reviews(models.Model):

	RATINGS_COUNT   = (
		('1','1'),
		('2','2'),
		('3','3'),
		('4','4'),
		('5','5'),

	)
	working_days    = (
		('Monday to Saturday','Monday to Saturday'),
		('Monday to Friday','Monday to Friday'),
		('Alternate Saturdays off','Alternate Saturdays off'),
		('Rotational shifts','Rotational shifts'),

	)
	WORKING         =   (
		('Normal','Normal'),
		('Strict','Strict'),
		('Flexible','Flexible'),
	)


	company         = models.ForeignKey(companies)
	name_or_title   = models.CharField(max_length=1000)
	dateposted      = models.DateField(null=True,auto_now_add=True)
	designation     = models.ForeignKey(designations)



	#RAtings
	skill_development_learning      = models.CharField(max_length=50,choices=RATINGS_COUNT,verbose_name="Skill development/learning")
	work_life_balance               = models.CharField(max_length=50,choices=RATINGS_COUNT,verbose_name='Work-Life balance')
	compensation_benifits           = models.CharField(max_length=50,choices=RATINGS_COUNT,verbose_name='Compensation & Benefits')
	company_culture                 = models.CharField(max_length=50,choices=RATINGS_COUNT,verbose_name='Company culture')
	job_security                    = models.CharField(max_length=50,choices=RATINGS_COUNT,verbose_name='Job Security')
	career_griwth_oppur             = models.CharField(max_length=50,choices=RATINGS_COUNT,verbose_name='Career growth & opportunities')
	work_statisfaction              = models.CharField(max_length=50,choices=RATINGS_COUNT,verbose_name='Work Satisfaction')


	working_days                    = models.CharField(max_length=200,choices=working_days,verbose_name='Working Days')
	job_travel                      = models.TextField()
	working_time                    = models.CharField(max_length=100,choices=WORKING)
	working_starttime               = models.TimeField()
	working_endtime                 = models.TimeField()

	likes                           = models.TextField()
	dislikes                        = models.TextField()



	def __str__(self):
		return  self.name_or_title + " | " + self.company.company_name





class  contacted(models.Model):
	name 		= models.CharField(max_length=1000)
	email 		= models.CharField(max_length=1000)
	subject 	= models.CharField(max_length=1000)
	comments 	= models.TextField()

	def __str__(self):
		return self.name + " | " + self.email


