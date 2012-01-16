from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template, redirect_to
from ecalife.eventcal.models import *
from eventcal.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'haha.views.home', name='home'),
    # url(r'^haha/', include('haha.foo.urls')),
    url(r'^$', 'ecalife.event.views.calendar_landing_page'),
##    url(r'^$', direct_to_template, { 'template': 'events/home.html'}, name='home'),
    (r'^events/(?P<yr>\d{4})/(?P<mm>\d{2})/(?P<dd>\d{2})/$','ecalife.event.views.month_listing'),
)
