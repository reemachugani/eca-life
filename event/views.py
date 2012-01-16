from datetime import datetime
from itertools import chain
from operator import attrgetter
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from event.forms import EventForm
from event.models import Event, EventFilter
from club.models import Member, Club
from announcement.models import Announcement
from profiles.models import StudentProfile
import datetime


def mk_paginator(request, items, num_items):
    """Create and return a paginator."""
    paginator = Paginator(items, num_items)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        items = paginator.page(page)
    except (InvalidPage, EmptyPage):
        items = paginator.page(paginator.num_pages)
    return items


@login_required
def add_event(request, pk):
    club = Club.objects.get(pk=pk)
    if request.POST:
        event = Event(club=club)
        form = EventForm(request.POST,instance=event )
        if form.is_valid():
            event = form.save()
            event.save()
            return render_to_response('event/successful_post.html', context_instance = RequestContext(request))

    else:
        form = EventForm()

    return render_to_response('club/add_event.html', {'form':form}, context_instance = RequestContext(request))


def event_page(request, pk):
    event = Event.objects.get(pk=pk)
    already_registered = False
    is_admin = False

    if request.user.is_authenticated():
        student = StudentProfile.objects.get(user=request.user)
        if student in event.registered.all():
            already_registered = True
        club = event.club
        if Member.objects.filter(club=club, student__user=request.user, admin=True):
            is_admin = True
    return render_to_response('event/event_page.html', {'event':event, 'is_admin':is_admin, 'already_registered':already_registered}, context_instance = RequestContext(request))


@login_required
def register(request, pk): # registering for an event
    event = Event.objects.get(pk=pk)
    already_there = False
    student = StudentProfile.objects.get(user=request.user)
    if student in event.registered.all():
        already_there = True
    if not already_there:
        event.registered.add(student)
        event.save()
    return render_to_response('event/successful_registration.html',{'already_there':already_there, 'event':event}, context_instance=RequestContext(request))


## used for showing with the calendar
@login_required
def registered_events(request):
    events = []
    for event in Event.objects.all():
        if request.user in event.registered.all:
            events.append(event)
    return render_to_response('event/registered.html',{'events':events}, context_instance=RequestContext(request))


#deprecated
@login_required
def myclub_events(request):
    events = []
    student = StudentProfile.objects.get(user = request.user)
    for club in Club.objects.all():
        if student in club.members.all():
            event = Event.objects.filter(club = club)
            events.extend(event)

    events.sort(key=attrgetter('date'), reverse=False)
    events = mk_paginator(request, events, 6)
    return render_to_response('event/myclub.html',{'events':events}, context_instance=RequestContext(request))


def all_events(request):
    events = []
    if request.user.is_authenticated():
        student = StudentProfile.objects.get(user = request.user)
    for club in Club.objects.all():
        for event in Event.objects.filter(club=club).filter(date__gte = datetime.datetime.now()):
##        for event in Event.objects.filter(club=club).filter(date__gte = datetime.now()):
            if event.viewership == 'P':
                events.append(event)
            if request.user.is_authenticated():
                if event.viewership == 'S':
                    events.append(event)
                if event.viewership == 'M' and (student in club.members.all()):
                    events.append(event)
    return events



def public_events(request):
    events = all_events(request)
    events.sort(key=attrgetter('date'), reverse=False)
    events = mk_paginator(request, events, 6)
    return render_to_response('event/allclubs.html',{'events':events}, context_instance=RequestContext(request))


@login_required
def registered_users(request, pk):
    event = Event.objects.get(pk=pk)
    students = event.registered.all()
    return render_to_response('event/registered_users.html',{'students':students, 'event':event}, context_instance=RequestContext(request))


def club_wise_events(request, pk):
    club = Club.objects.get(pk=pk)
    events = Event.objects.filter(club=club)
    events = mk_paginator(request, events, 6)
    return render_to_response('club/club_wise_events.html',{'events':events},context_instance=RequestContext(request))


def delete_event(request, pk):
    event = Event.objects.get(pk=pk)
    event.delete()
    return render_to_response('event/event_deleted.html', context_instance=RequestContext(request))


# filtering events
def event_list(request):
    student = []
    events = []
    f = EventFilter(request.GET, queryset=Event.objects.all())
    if request.user.is_authenticated():
        student = StudentProfile.objects.get(user = request.user)

    event = Event.objects.filter(date__lt = datetime.datetime.now())
    event.delete()

    for event in f:
        events.append(event)

    events.sort(key=attrgetter('date'))
    events = mk_paginator(request, events, 6)
    return render_to_response('event/filter.html', {'filter':f, 'student':student, 'events':events}, context_instance=RequestContext(request))


def calendar_landing_page(request):
    now=datetime.datetime.now()
    year =  now.year
    month= now.month
    day= now.day
    return month_listing(request,year,month,day)

    
    

def month_listing(request,yr,mm,dd):
    yr1=int(yr)
    mm1=int(mm)
    dd1=int(dd)
    event= all_events(request)
    eventdetail=Event.objects.filter(date=datetime.date(yr1,mm1,dd1))
    events = []
    for i in eventdetail:
        for j in event:
            if i == j:
                events.append(j)
    
    has_event=False

    if events:
        has_event=True
            

            
    return render_to_response('events/calendar.html',{'eventdetail':events,'has_event':has_event},context_instance=RequestContext(request))


