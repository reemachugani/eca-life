from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.db.models.signals import post_save
from datetime import timedelta
import datetime
from club.models import Club, Member
from profiles.models import StudentProfile
        
class Forum(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=144)
    club = models.ForeignKey(Club)
    
    def __unicode__(self):
        return self.club + " - " + self.title 

    def num_threads(self):
        return self.thread_set.count()

class Thread(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    forum = models.ForeignKey(Forum)
    
    class Meta:
        ordering = ["-created"]

    def __unicode__(self):
        return unicode(self.creator) + " - " + self.title

    def num_posts(self):
        return self.post_set.count()

    def num_replies(self):
        return self.post_set.count() - 1
    
    def num_views(self):
        return self.threadview_set.count()

    def last_post(self):
        if self.post_set.count():
            return self.post_set.order_by("created")[0]

class ThreadView(models.Model):
    """To track the number of views of each thread"""
    thread = models.ForeignKey(Thread)
    ip = models.CharField(max_length=40)
    session = models.CharField(max_length=40)
    created = models.DateTimeField(default=datetime.datetime.now())
        
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    thread = models.ForeignKey(Thread)
    body = models.TextField(max_length=10000)
    first_post = models.BooleanField()
        
    class Meta:
        ordering = ["created"]

    def __unicode__(self):
        return u"%s - %s - %s" % (self.creator, self.thread, self.title)

    def short(self):
        return u"%s - %s\n%s" % (self.creator, self.title, self.created.strftime("%b %d, %I:%M %p"))
    short.allow_tags = True

    def profile_data(self):
        p = StudentProfile.objects.get(user=self.creator)
        return p.posts, p.avatar


class ForumAdmin(admin.ModelAdmin):
    list_display = ['title', 'club', 'description']
    
class ThreadAdmin(admin.ModelAdmin):
    list_display = ["title", "forum", "creator", "created"]
    list_filter = ["forum", "creator"]
    
class ThreadViewAdmin(admin.ModelAdmin):
    list_display = ["ip", "thread", "created"]
    list_filter = ["thread", "created"]
    
class PostAdmin(admin.ModelAdmin):
    search_fields = ["title", "creator"]
    list_display = ["title", "thread", "creator", "created"]