from django.conf.urls import patterns, url
from pb import views
# from pb.views import some class base views
from django.conf import settings


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.login_user, name='login_user'),
        url(r'request/(?P<request_id>[0-9]+)/$', views.get_request, name='get_request'),
        url(r'isrequestpaid/(?P<request_id>[0-9]+)/$', views.is_request_paid, name='is_request_paid'),
        
        # Ajax
        url(r'^submitrequestdata/$', views.submit_request_data, name='submit_request_data'),

        url(r'getcompanies/(?P<bill_type>[-\w]+)/$', views.get_companies, name='get_companies'),
        url(r'timeleft/(?P<request_id>[0-9]+)/$', views.time_left_to_pay, name='time_left_to_pay'),


        url(r'^logout/$', views.user_logout, name='logout'),)
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}),)
#-------------------------------------
# ----------- Merchent Area-----------
#-------------------------------------
# Paymets -----------
#--------------------
# Approved Payments
# Pending Payments
# Paid Payments
# OnHold Payments
#-----------------------------
# Dashboard and Requests -----
#-----------------------------
# Pending Requests
# To be Processed Requests
#-----------------------------
# Sign up and Login -----
#-----------------------------
# Pending Requests
# To be Processed Requests
#-------------------------------------
# ----------- Frontend Users ---------
#-------------------------------------
# Submit Request -----------
#---------------------------
# Main details
# 