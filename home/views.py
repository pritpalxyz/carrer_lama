# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from .forms import *



class indexView(TemplateView):
    template_name = "home.html"


    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        #DEFAULT CALLS
        alldesignations         = designations.objects.all().order_by('designation_name')
        allindustries           = category.objects.all().order_by('category_name')
        alllocations            = States.objects.all().order_by('state_name')
        allhomecompanies        = companies.objects.all().order_by('company_name')[:6]
        latestReviews           = reviews.objects.all().order_by('-id')[:5]

        allcompaniesCount       = companies.objects.all().count()
        allreviewsCount         = reviews.objects.all().count()


        context['alldesignations']  = alldesignations
        context['allindustries']    = allindustries
        context['alllocations']     = alllocations
        context['allhomecompanies'] = allhomecompanies
        context['latestReviews']    = latestReviews

        context['allcompaniesCount']  = allcompaniesCount
        context['allreviewsCount'] = allreviewsCount

        return context

class companyView(TemplateView):
    template_name   = "company.html"




    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        #DEFAULT CALLS
        alldesignations         = designations.objects.all().order_by('designation_name')
        allindustries           = category.objects.all().order_by('category_name')
        alllocations            = States.objects.all().order_by('state_name')
        allhomecompanies        = companies.objects.all().order_by('company_name')[:6]
        latestReviews           = reviews.objects.all().order_by('-id')[:5]

        allcompaniesCount       = companies.objects.all().count()
        allreviewsCount         = reviews.objects.all().count()


        context['alldesignations']  = alldesignations
        context['allindustries']    = allindustries
        context['alllocations']     = alllocations
        context['allhomecompanies'] = allhomecompanies
        context['latestReviews']    = latestReviews

        context['allcompaniesCount']  = allcompaniesCount
        context['allreviewsCount'] = allreviewsCount

        # Particulars calls

        pk = self.kwargs['pk']
        comp        = companies.objects.get(pk=pk)
        allreviews          = reviews.objects.filter(company=comp).order_by('-id')
        context['comp'] = comp
        context['allreviews'] = allreviews

        return context

class allcompaniesView(TemplateView):
    template_name = "allcompanies.html"



    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        #DEFAULT CALLS

        query = self.request.GET.get('q')
        if query is not None:

            allhomecompanies = companies.objects.filter(company_name__contains=query).order_by('company_name')
            context['query'] = query
        else:
            allhomecompanies = companies.objects.all().order_by('company_name')


        alldesignations         = designations.objects.all().order_by('designation_name')
        allindustries           = category.objects.all().order_by('category_name')
        alllocations            = States.objects.all().order_by('state_name')

        latestReviews           = reviews.objects.all().order_by('-id')[:5]
        allcompaniesCount       = companies.objects.all().count()
        allreviewsCount         = reviews.objects.all().count()


        context['alldesignations']  = alldesignations
        context['allindustries']    = allindustries
        context['alllocations']     = alllocations
        context['latestReviews']    = latestReviews
        context['allcompaniesCount']  = allcompaniesCount
        context['allreviewsCount'] = allreviewsCount





        paginator = Paginator(allhomecompanies, 8)

        page = self.request.GET.get('page')
        try:
            allhomecompanies = paginator.page(page)
        except PageNotAnInteger:
            allhomecompanies = paginator.page(1)
        except EmptyPage:
            allhomecompanies = paginator.page(paginator.num_pages)

        context['allhomecompanies'] = allhomecompanies

        return context

class category_wiseView(TemplateView):
    template_name = "category_wise.html"

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        # DEFAULT CALLS

        categoryid          = self.kwargs['pk']

        alldesignations = designations.objects.all().order_by('designation_name')
        allindustries = category.objects.all().order_by('category_name')
        alllocations = States.objects.all().order_by('state_name')
        allhomecompanies = companies.objects.filter(category=categoryid).order_by('company_name')
        latestReviews = reviews.objects.all().order_by('-id')[:5]
        allcompaniesCount = companies.objects.all().count()
        allreviewsCount = reviews.objects.all().count()

        context['alldesignations'] = alldesignations
        context['allindustries'] = allindustries
        context['alllocations'] = alllocations
        context['latestReviews'] = latestReviews
        context['allcompaniesCount'] = allcompaniesCount
        context['allreviewsCount'] = allreviewsCount

        paginator = Paginator(allhomecompanies, 8)

        page = self.request.GET.get('page')
        try:
            allhomecompanies = paginator.page(page)
        except PageNotAnInteger:
            allhomecompanies = paginator.page(1)
        except EmptyPage:
            allhomecompanies = paginator.page(paginator.num_pages)

        context['allhomecompanies'] = allhomecompanies

        return context

class location_wiseView(TemplateView):
    template_name = "location_wise.html"

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        # DEFAULT CALLS

        locid = self.kwargs['pk']

        alldesignations = designations.objects.all().order_by('designation_name')
        allindustries = category.objects.all().order_by('category_name')
        alllocations = States.objects.all().order_by('state_name')
        allhomecompanies = companies.objects.filter(state=locid).order_by('company_name')
        latestReviews = reviews.objects.all().order_by('-id')[:5]
        allcompaniesCount = companies.objects.all().count()
        allreviewsCount = reviews.objects.all().count()

        context['alldesignations'] = alldesignations
        context['allindustries'] = allindustries
        context['alllocations'] = alllocations
        context['latestReviews'] = latestReviews
        context['allcompaniesCount'] = allcompaniesCount
        context['allreviewsCount'] = allreviewsCount

        paginator = Paginator(allhomecompanies, 8)

        page = self.request.GET.get('page')
        try:
            allhomecompanies = paginator.page(page)
        except PageNotAnInteger:
            allhomecompanies = paginator.page(1)
        except EmptyPage:
            allhomecompanies = paginator.page(paginator.num_pages)

        context['allhomecompanies'] = allhomecompanies

        return context


class term_conditionView(TemplateView):
    template_name = "terms_conditions.html"


class write_reviewView(TemplateView):
    template_name = "write.html"


    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)

        alldesignations = designations.objects.all().order_by('designation_name')
        allindustries = category.objects.all().order_by('category_name')
        alllocations = States.objects.all().order_by('state_name')
        allhomecompanies = companies.objects.all().order_by('company_name')[:6]
        latestReviews = reviews.objects.all().order_by('-id')[:5]

        allcompaniesCount = companies.objects.all().count()
        allreviewsCount = reviews.objects.all().count()

        context['alldesignations'] = alldesignations
        context['allindustries'] = allindustries
        context['alllocations'] = alllocations
        context['allhomecompanies'] = allhomecompanies
        context['latestReviews'] = latestReviews

        context['allcompaniesCount'] = allcompaniesCount
        context['allreviewsCount'] = allreviewsCount


        companyid               =   self.kwargs['pk']
        compinsta               = companies.objects.get(pk=companyid)
        context['compinsta']    = compinsta

        timedict = []
        for i in range(1,25):
            # print i
            sizeofi = len(str(i))
            if sizeofi == 1:
                pretime     = "0{0}:00:00".format(i)
                timedict.append(pretime)
                pretime    = "0{0}:30:00".format(i)
                timedict.append(pretime)
            else:
                pretime     = "{0}:00:00".format(i)
                timedict.append(pretime)
                pretime    = "{0}:30:00".format(i)
                timedict.append(pretime)


        context['timedict'] =  timedict


        return context

def submit_review(request):
    if request.method == 'POST':



        company                         = request.POST['compid']
        name_or_title                   = request.POST['name']

        designation                     = request.POST['designation']

        skill_development_learning      = request.POST['skill_develop']

        work_life_balance               = request.POST['work_life']
        compensation_benifits           = request.POST['compensation']

        company_culture                 = request.POST['company_cul']
        job_security                    = request.POST['job_security']
        career_griwth_oppur             = request.POST['career_growth']
        work_statisfaction              = request.POST['work_satis']

        working_days                    = request.POST['working_days']
        job_travel                      = request.POST['job_travel']
        working_time                    = request.POST['working_time']
        working_starttime               = request.POST['start_time']
        working_endtime                 = request.POST['end_time']

        likes                           = request.POST['likes']
        dislikes                        = request.POST['dislike']
        print "POST REQUEST"

        compinsta                    =   companies.objects.get(pk=company)
        desiginsta                   = designations.objects.get(pk=designation)

        reviewinsta                                  = reviews(company=compinsta)
        reviewinsta.name_or_title                    = name_or_title
        reviewinsta.designation                      = desiginsta
        reviewinsta.skill_development_learning       = skill_development_learning
        reviewinsta.work_life_balance                 =  work_life_balance
        reviewinsta.compensation_benifits   = compensation_benifits
        reviewinsta.company_culture         = company_culture
        reviewinsta.job_security            = job_security
        reviewinsta.career_griwth_oppur     = career_griwth_oppur
        reviewinsta.work_statisfaction      = work_statisfaction
        reviewinsta.working_days            = working_days
        reviewinsta.job_travel              = job_travel
        reviewinsta.working_time            = working_time
        reviewinsta.working_starttime       = working_starttime
        reviewinsta.working_endtime         = working_endtime
        reviewinsta.likes                   = likes
        reviewinsta.dislikes                = dislikes
        reviewinsta.save()
        return HttpResponseRedirect(reverse('home:company',args=(company,)))


    else:
        return HttpResponse("Not Allowed")
        print "GET REQUEST"





class contactView(FormView):
    template_name = "contact.html"
    form_class = addContactedForm
    success_url = '/contact/'

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Thanks for contacting us..!!")
        return super(self.__class__, self).form_valid(form)





index           = indexView.as_view()
company         = companyView.as_view()
allcompanies    = allcompaniesView.as_view()
category_wise   = category_wiseView.as_view()
location_wise   = location_wiseView.as_view()
term_condition  = term_conditionView.as_view()
write_review    = write_reviewView.as_view()
contact         = contactView.as_view()