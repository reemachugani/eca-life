from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import get_object_or_404, render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from forms import PostForm, CommentForm, ForumForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from settings import MEDIA_ROOT, MEDIA_URL
from forum.models import *
from club.models import Club, Member
from avatar.models import Avatar
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

def add_csrf(request, **kwargs):
    """Short cut function to add CSRF to dictionary."""
    d = dict(user=request.user, **kwargs)
    d.update(csrf(request))
    return d

def main(request):
    """List of available forums and topics to be shown in landing page"""
    forums = []
    list = []
    if request.user.is_authenticated():
        student = StudentProfile.objects.get(user = request.user)
        for club in Club.objects.all():
            if student in club.members.all():
                forum = Forum.objects.filter(club=club)
                forums.append(forum)
                list.extend(forum)
    has_forum = True
    if len(list) == 0:
        has_forum = False
     
    return render_to_response("forum/index.html", add_csrf(request, forums=forums,has_forum=has_forum), 
                    context_instance=RequestContext(request))

def forum(request, pk):
    """List of threads in a forum."""
    forum = Forum.objects.get(pk=pk)
    threads = Thread.objects.filter(forum=pk)
    # 8 threads a page
    threads = mk_paginator(request, threads, 8)
    return render_to_response("forum/forum.html", add_csrf(request, forum=forum, threads=threads, pk=pk), 
                    context_instance=RequestContext(request))
 
@login_required  
def club_wise_forums(request, pk):
    club = Club.objects.get(pk=pk)
    forums = Forum.objects.filter(club=club)
    is_admin = False
    if Member.objects.filter(club=club, student__user=request.user, admin=True):
        is_admin = True
    return render_to_response('forum/club_wise_forums.html',{'forums':forums, 'club_pk':pk, 'is_admin':is_admin}, 
                    context_instance=RequestContext(request))

@login_required
def new_forum(request, pk):
    """Add a new forum for club"""  
    if request.method == 'POST':
        p = request.POST
        form = ForumForm(p)
        if form.is_valid():
            club = Club.objects.get(pk=pk)
            forum = Forum.objects.create(title=p['title'], description=p['description'], club=club)
            return HttpResponseRedirect(reverse('club.views.club_page', args=[pk]))
    else:
        form = ForumForm()
    return render_to_response('forum/new_forum.html', {'form':form}, 
                    context_instance = RequestContext(request))

@login_required
def delete_forum(request, pk):
    """Delete specified forum."""
    forum = get_object_or_404(Forum, pk=pk)
    club = Club.objects.get(forum=forum)
    student = StudentProfile.objects.get(user=request.user)
    # check if the user is actually adminstrator - by right only admin should have the link
    # if the user is obtaining the link is not admin, raise Http404.
    if Member.objects.filter(club=club, student__user=request.user, admin=True):    
        forum.delete()
    else:
        raise Http404
    return club_wise_forums(request, club.pk)

def increment_post_counter(request):
    """Whenever a thread is started or user make a comment"""
    profile = StudentProfile.objects.get(user=request.user)
    profile.posts += 1
    profile.save()


def thread(request, pk):
    """List of posts in a thread."""
    user = request.user
    try:
        profile_obj = user.get_profile()
    except ObjectDoesNotExist:
        raise Http404
    posts = Post.objects.filter(thread=pk)
    
    # # 20 posts in a page, can be furthered improved using ajax load on scroll
    posts = mk_paginator(request, posts, 20)
    
    views = thread_view(request, pk)
    thread = Thread.objects.get(pk=pk)
    
    is_owner = False
    if thread.creator == request.user:
        is_owner = True
    is_admin = False
    forum = Forum.objects.get(thread__pk=pk)
    club = Club.objects.get(forum=forum)
    student = StudentProfile.objects.get(user=request.user)
    if Member.objects.filter(club=club, student__user=request.user, admin=True):
        is_admin = True
        
    if request.method == 'POST':
        p = request.POST
        form = CommentForm(p)
        if form.is_valid():
            Post.objects.create(thread=thread, title="re:%s" %thread.title, body=p['body'], creator=request.user, first_post=False)
            increment_post_counter(request)
            return HttpResponseRedirect(reverse("forum.views.thread", args=[thread.pk]) + "?page=last")
    else:
        form = CommentForm()
    
    return render_to_response("forum/thread.html", add_csrf(request, views=views, posts=posts, 
                    pk=pk, thread=thread, forum_pk=thread.forum.pk, form=form, profile=profile_obj, is_admin=is_admin, is_owner=is_owner), 
                    context_instance=RequestContext(request))
                                                           
def thread_view(request, thread_id):
    """Get the number of views of thread"""
    thread = get_object_or_404(Thread, pk=thread_id)
    
    if not ThreadView.objects.filter(
                    thread=thread,
                    session=request.session.session_key):
        view = ThreadView(
                    thread=thread,
                    ip=request.META['REMOTE_ADDR'],
                    created=datetime.datetime.now(),
                    session=request.session.session_key)
        view.save()
    return (u"%s" % ThreadView.objects.filter(thread=thread).count())


@login_required
def new_thread(request, pk):
    """Start a new thread."""
    if request.method == 'POST':
        p = request.POST
        form = PostForm(p)
        if form.is_valid():
            forum = Forum.objects.get(pk=pk)
            thread = Thread.objects.create(forum=forum, title=p['title'], creator=request.user)
            Post.objects.create(thread=thread, title=p['title'], body=p['body'], creator=request.user, first_post=True)
            increment_post_counter(request)
            return HttpResponseRedirect(reverse('forum.views.forum', args=[pk]))
    else:
        form = PostForm()
    
    return render_to_response('forum/new_thread.html', add_csrf(request, form=form), 
                    context_instance=RequestContext(request))
                

@login_required
def edit_post(request, pk_thread=None, pk_post=None):
    """Edit a thread."""
    post = get_object_or_404(Post, pk=pk_post)   
    thread = get_object_or_404(Thread, pk=pk_thread)
    forum = Forum.objects.get(thread__pk=pk_thread)

    is_admin = False
    club = Club.objects.get(forum=forum)
    student = StudentProfile.objects.get(user=request.user)
    if Member.objects.filter(club=club, student__user=request.user, admin=True):
        is_admin = True
        
    if pk_post:
        post = get_object_or_404(Post, pk=pk_post)
        if post.creator != request.user and is_admin == False:
            raise Http404
    else:
        post = Post(creator=request.user)
            
    if request.POST:
        form = CommentForm(request.POST, instance=post)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse("forum.views.thread", args=[pk_thread]) + "?page=last")   
    else:
        form = CommentForm(instance=post)
    
    return render_to_response('forum/post_edit.html', add_csrf(request, form=form), context_instance=RequestContext(request)) 


@login_required 
def delete_post(request, pk_thread=None, pk_post=None):
    """Delete specified post."""
    post = get_object_or_404(Post, pk=pk_post)   
    thread = get_object_or_404(Thread, pk=pk_thread)
    forum = Forum.objects.get(thread__pk=pk_thread)
    
    club = Club.objects.get(forum=forum)
    student = StudentProfile.objects.get(user=request.user)
    if Member.objects.filter(club=club, student__user=request.user, admin=True):    
        if post.first_post:
            thread.delete()
            # this is just to get the page to the forum list
            return HttpResponseRedirect('deleted.html')
        else:
            post.delete()
    else:
        raise Http404
    return HttpResponseRedirect(reverse("forum.views.thread", args=[pk_thread]) + "?page=last")   
                 
                
