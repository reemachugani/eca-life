from django.contrib import admin
from ecalife.announcement.models import Announcement
from django.contrib.sites.models import Site

admin.site.register(Announcement)