from django.conf.urls import patterns, url
from pb import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))