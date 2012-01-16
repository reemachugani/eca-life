from datetime import datetime
from operator import attrgetter
from django.core.paginator import InvalidPage, EmptyPage, Paginator
from django.db.models.query_utils import Q
from django.shortcuts import render_to_response
from django.template import RequestContext
from announcement.models import Announcement
from club.models import Club, Member
from event.models import Event
from profiles.models import StudentProfile
from event.views import all_events
from announcement.views import announcements


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


def search(request):
    query = request.GET.get('q', '')
    club = []
    announce = []
    event = []
    if query:
        club = Club.objects.filter(Q(name__icontains = query) |
                                   Q(name__iexact = query) |
                                   Q(name__in = query.split())).distinct().filter(is_active = True)
        ann = Announcement.objects.filter(Q(announcement__icontains = query) |
                                               Q(announcement__iexact = query) |
                                               Q(announcement__in = query.split())).distinct()
        event = Event.objects.filter(Q(title__icontains = query) |
                                     Q(announcement__icontains = query) |
                                     Q(title__iexact = query) |
                                     Q(announcement__iexact = query) |
                                     Q(title__in = query.split()) |
                                     Q(announcement__in = query.split())
                                     ).distinct()
    events = all_events(request)
    eventresult = []
    for i in event:
        for j in events:
            if i == j:
                eventresult.append(j)
                
    anns = announcements(request)
    annresult = []
    for i in announce:
        for j in anns:
            if i == j:
                annresult.append(j)

##    club = mk_paginator(request, club, 5)
##    eventresult = mk_paginator(request, eventresult, 5)
##    annresult = mk_paginator(request, annresult, 5)


    return render_to_response('search/search.html', {'club':club, 'event':eventresult, 'announce':annresult, 'query':query}, context_instance=RequestContext(request))


#
#def filter(request, field):
#    result = []
#    if request.GET:
#        form = FilterForm(request.GET)
#
#        query = request.GET['category']
#        if field is "clubs":
#            if query is '10' and request.user.is_authenticated():
#                members = Member.objects.filter(student__user = request.user)
#                for member in members:
#                    if member.club.is_active:
#                        result.append(member.club)
#            else:
#                result = Club.objects.filter(category__iexact = query).filter(is_active = True).distinct()
#
#            result.sort(key=attrgetter('name'), reverse=False)
##                return render_to_response('club/filter.html', {'field':field, 'result':result}, context_instance=RequestContext(request))
#
#
#        if field is "events":
#            if query is '10' and request.user.is_authenticated():
#                student = StudentProfile.objects.get(user = request.user)
#                for club in Club.objects.all():
#                    if student in club.members.all():
#                        event = Event.objects.filter(club = club).filter(date__gte = datetime.now())
#                        result.extend(event)
#            else:
#                result = Event.objects.filter(club__category__iexact = query).filter(club__is_active = True).filter(date__gte = datetime.now()).distinct()
#
#            result.sort(key=attrgetter('date'), reverse=False)
##                return render_to_response('event/filter.html', {'field':field, 'result':result}, context_instance=RequestContext(request))
#
#    else:
#        form = FilterForm()
#
#    if field == "clubs":
#        return render_to_response('club/filter.html', {'form':form, 'result':result}, context_instance=RequestContext(request))
#    else:
#        return render_to_response('event/filter.html', {'form':form, 'result':result}, context_instance=RequestContext(request))
