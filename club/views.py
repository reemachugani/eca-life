from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import InvalidPage, EmptyPage, Paginator
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.core.context_processors import csrf
from club.forms import ClubForm
from club.models import Club, Member, ClubFilter
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


def all_clubs(request):
    clubs = Club.objects.filter(is_active = True)
    return render_to_response('club/club_index.html', {'clubs':clubs}, context_instance=RequestContext(request))



@login_required
def my_clubs(request):
    members = Member.objects.filter(student__user = request.user)
    clubs = []
    for member in members:
        if member.club.is_active:
            clubs.append(member.club)
    clubs = mk_paginator(request, clubs, 6)
    return render_to_response('club/my_clubs.html', {'clubs':clubs}, context_instance=RequestContext(request))



def club_page(request, pk):
    club = Club.objects.get(pk=pk)
    admins = Member.objects.filter(club=club, admin=True)
    already_member = False
    for member in club.members.all():
        if request.user == member.user:
            already_member = True
    return render_to_response('club/club_page.html', {'club':club, 'admins':admins, 'already_member':already_member }, context_instance=RequestContext(request))



@login_required
@csrf_exempt
def add_club(request):
    if request.method == 'POST':
        form = ClubForm(request.POST)
        if form.is_valid():
            club = form.save()
            club.save()
            member = Member(club=club, student=StudentProfile.objects.get(user=request.user), admin=True)
            member.save()
            return render_to_response('club/club_confirmation_message.html', context_instance=RequestContext(request))

    else:
        form = ClubForm()

    return render_to_response('club/add_club.html', {'form':form}, context_instance=RequestContext(request))



@login_required
def become_member(request, pk):
    club = Club.objects.get(pk=pk)
    already_there = False
    if StudentProfile.objects.get(user=request.user) in club.members.all():
        already_there = True
    else:
        member = Member(club=club, student=StudentProfile.objects.get(user=request.user), admin=False)
        member.save()
    return render_to_response('club/membership_confirmed.html',{'club':club, 'already_there':already_there},context_instance=RequestContext(request))


def club_list(request):
    f = ClubFilter(request.GET, queryset=Club.objects.all())
    clubs = []
    for club in f:
        clubs.append(club)
    clubs = mk_paginator(request, clubs, 6)
    return render_to_response('club/filter.html', {'filter':f, 'clubs':clubs}, context_instance=RequestContext(request))
