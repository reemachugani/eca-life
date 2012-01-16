from club.admin import MemberInline
from ecalife.profiles.models import StudentProfile
from django.contrib import admin
from django.contrib.sites.models import Site
from django.conf import settings

class StudentProfileAdmin(admin.ModelAdmin):
    inlines = (MemberInline,)

admin.site.register(StudentProfile, StudentProfileAdmin)

