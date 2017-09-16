from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'all-companies/$',views.allcompanies,name='allcompanies'),

    url(r'all-companies-category/(?P<pk>[0-9a-z-]+)/$',views.category_wise,name='category_wise'),
    url(r'all-companies-location/(?P<pk>[0-9a-z-]+)/$',views.location_wise,name='location_wise'),

    url(r'company/(?P<pk>[0-9a-z-]+)/$',views.company,name='company'),


    url(r'write-review/(?P<pk>[0-9a-z-]+)/$',views.write_review,name='write_review'),

    url(r'submit-review/$',views.submit_review,name='submit_review'),

    url(r'contact/$',views.contact,name='contact'),


    url(r'terms-conditions/$',views.term_condition,name='term_condition'),



]