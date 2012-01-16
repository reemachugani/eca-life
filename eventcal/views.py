from django.template import RequestContext
from django.db import models
from event.models import Event
from django.shortcuts import get_object_or_404, render_to_response
import datetime

from django import http

def month_listing(request,yr,mm,dd):
##    start_date=datetime.date(yr,mm,dd)
##    end_date=datetime.date(yr,mm,dd)
    yr1=int(yr)
    mm1=int(mm)
    dd1=int(dd)
    
    eventdetail=Activity.objects.filter(eventdate=datetime.date(yr1,mm1,dd1))
    return render_to_response('events/calendar.html',{'eventdetail':eventdetail},context_instance=RequestContext(request))
    
