from django.conf.urls import patterns, url
from pb import views
# from pb.views import some class base views
from django.conf import settings


urlpatterns = patterns('',
        # Public info pages for everyone
        url(r'^$', views.index, name='index'),

        # Merchent Section
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.login_user, name='login_user'),
        # Merchent Bill Processing Requests
        url(r'claim/(?P<request_id>[0-9]+)/$', views.claim_request, name='claim_request'),
        url(r'confirm-request/(?P<request_id>[0-9]+)/$', views.confirm_request, name='confirm_request'),
        url(r'mercehenttimeleft/(?P<request_id>[0-9]+)/$', views.merchent_time_left, name='merchent_time_left'),
        url(r'latest-requests/$', views.bill_requests, name='bill_requests'),
        url(r'completed-requests/$', views.merchent_completed_requests, name='merchent_completed_requests'),
        url(r'claimed-requests/$', views.merchent_claimed_requests, name='merchent_claimed_requests'),
        url(r'dashboard/$', views.merchent_dashboard, name='merchent_dashboard'),
        # Merchent Payments
        url(r'payments/$', views.all_payments, name='all_payments'),
        url(r'createpayment/$', views.create_payment, name='create_payment'),
        # Merchent Settings
        url(r'settings/password/$', views.change_password, name='change_password'),

        # Ajax for front-end user who submits bill request!
        url(r'^track/$', views.track_bill_request, name='track_bill_request'),
        url(r'^submitrequestdata/$', views.submit_request_data, name='submit_request_data'),
        url(r'getcompanies/(?P<bill_type>[-\w]+)/$', views.get_companies, name='get_companies'),
        url(r'timeleft/(?P<request_id>[0-9]+)/$', views.time_left_to_pay, name='time_left_to_pay'),
        url(r'isrequestpaid/(?P<request_id>[0-9]+)/$', views.is_request_paid, name='is_request_paid'),

        # Logout for merchents
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