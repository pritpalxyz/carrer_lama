from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    url(r'^$',views.index,name='index'),

    url(r'write-a-review/$',views.writeAReview,name='writeAReview'),
    url(r'submit-phase-one/$', views.submitPhaseOne, name='submitPhaseOne'),
    url(r'write-review/(?P<pk>[0-9a-z-]+)/$',views.writeReviewRest,name='writeReviewRest'),
    url(r'submit-phase-two/$',views.submitPhaseTwo,name='submitPhaseTwo'),
    url(r'thanks/$',views.thanks_page,name='thanks_page'),


    url(r'company/(?P<pk>[0-9a-z-]+)/$',views.company,name='company'),


    url(r'login/$',views.login,name='login'),
    url(r'login-check/$',views.login_check,name='login_check'),

    url(r'logout/$',views.logoutUser,name='logoutUser'),

    url(r'register/$',views.register,name='register'),
    url(r'register-me/$',views.register_me,name='register_me'),

    url(r'update-user-profile/$', views.update_user_profile, name='update_user_profile'),
    # url(r'update-user-image/$',views.updateUserImage,name='updateUserImage'),
    url(r'user-profile/$',views.profile,name='profile'),



    url(r'get-all-companies/$',views.get_all_companies,name='get_all_companies'),
    url(r'write-sub-process/$',views.writeSubProcess,name='writeSubProcess'),
    url(r'delete-sub-process/$',views.deleteSubProcess,name='deleteSubProcess'),



]