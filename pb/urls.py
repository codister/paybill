from django.conf.urls import patterns, url
from pb import views
from django.conf import settings


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.login_user, name='login_user'),
        url(r'^settings/$', views.settings, name='settings'),)
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