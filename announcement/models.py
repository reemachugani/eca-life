from django.db import models
from club.models import Club

VIEWERSHIP = (
    ('M','Only Members'),
    ('S','All Students'),
    ('P','Public (Guests too)'),
)

class Announcement(models.Model):
    announcement = models.TextField(max_length=500)
    date_posted = models.DateField(auto_now_add=True)
    club = models.ForeignKey(Club)
    viewership = models.CharField(max_length=1, choices=VIEWERSHIP)

    def __unicode__(self):
        return self.club + " : " + self.announcement