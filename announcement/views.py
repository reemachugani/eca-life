from itertools import chain
from operator import attrgetter
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import InvalidPage, EmptyPage, Paginator
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from announcement.forms import AnnouncementForm
from announcement.models import Announcement
from club.models import Club, Member
from event.models import Event
from profiles.models import StudentProfile


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
@csrf_exempt
def announce(request, pk):
    club = Club.objects.get(pk=pk)
    if request.POST:
        announce = Announcement(club=club)
        form = AnnouncementForm(request.POST,instance=announce )
        if form.is_valid():
            announce = form.save()
            announce.save()
            return render_to_response('announcement/successful_post.html', context_instance = RequestContext(request))
    else:
        form = AnnouncementForm()
            
    return render_to_response('club/make_announcement.html', {'form':form}, context_instance = RequestContext(request) )


def announcements(request):
    all_announcements = []
    clubs = Club.objects.all()
    if request.user.is_authenticated():
        student = StudentProfile.objects.get(user = request.user)
    for club in clubs:
        for announcement in club.announcement_set.all():
            if announcement.viewership == 'P':
                all_announcements.append(announcement)
            if request.user.is_authenticated():
                if announcement.viewership == 'S':
                    all_announcements.append(announcement)
                if announcement.viewership == 'M' and request.user.is_authenticated():
                    if student in club.members.all():
                        all_announcements.append(announcement)

    return all_announcements



def homepage(request):
    announcement = announcements(request)
    announcement.sort(key=attrgetter('date_posted'), reverse=True)
    announcement = mk_paginator(request, announcement, 6)
    return render_to_response('announcement/homepage.html',{'announcements':announcement}, context_instance=RequestContext(request))


@login_required
def myclub_announce(request):
    announcements = []
    student = StudentProfile.objects.get(user = request.user)
    for club in Club.objects.all():
        if student in club.members.all():
            announce = Announcement.objects.filter(club=club)
            announcements.extend(announce)

    announcements.sort(key=attrgetter('date_posted'), reverse=True)

    announcements = mk_paginator(request, announcements, 6)

    return render_to_response('announcement/myclub.html',{'announcements':announcements}, context_instance=RequestContext(request))


def club_wise_announce(request, pk):
    club = Club.objects.get(pk=pk)
    announcements = Announcement.objects.filter(club=club)
    announcements = mk_paginator(request, announcements, 6)
    return render_to_response('club/club_wise_announce.html',{'announcements':announcements},context_instance=RequestContext(request))
