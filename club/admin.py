from django.contrib import admin
from django.contrib.sites.models import Site
from django.conf import settings
from club.models import Club, Member

class MemberInline(admin.TabularInline):
    model = Member
    extra = 1

class ClubAdmin(admin.ModelAdmin):
    inlines = (MemberInline,)
    
admin.site.register(Club, ClubAdmin)