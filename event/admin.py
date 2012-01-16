from django.contrib import admin
from ecalife.event.models import Event
from django.contrib.sites.models import Site

admin.site.register(Event)