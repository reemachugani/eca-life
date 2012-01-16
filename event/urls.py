from django.conf.urls.defaults import *
from event.views import *
from django.template import RequestContext
from django.db import models
from django.shortcuts import get_object_or_404, render_to_response
import datetime
from django.views.generic.simple import direct_to_template, redirect_to


urlpatterns = patterns('',
#    (r'^$', public_events),
    (r'^my_club_events/$', myclub_events),
    (r'^(\d+)/$', event_page),
    (r'^(\d+)/register/$', register),
    (r'^(\d+)/registered_users/$', registered_users),
    (r'^(\d+)/delete/$', delete_event),
    (r'^$', event_list),
    url(r'^$', direct_to_template, { 'template': 'events/home.html'}, name='home'),

)
