from django.db import models
import django_filters
from ecalife.profiles.models import StudentProfile


CLUB_CATEGORY = (('', 'All Clubs'),
                 ('1', 'Students\' Union Clubs'),
                 ('2', 'Sports Clubs'),
                 ('3', 'Academic Clubs'),
                 ('4', 'Cultural Activities Clubs'),
                 ('5', 'Career Clubs'),
                 ('6', 'Investment & Finance Clubs'),
                 ('7', 'Technology-related Clubs'),
                 ('8', 'Skill-building Clubs'),
                 ('9', 'Others'),
)

class Club(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()
    is_active = models.BooleanField(default=False)
    category = models.CharField(max_length=2, choices=CLUB_CATEGORY)
    members = models.ManyToManyField(StudentProfile, through='Member')
#    image = models.ImageField(upload_to='images/', blank=True)

    def __unicode__(self):
        return self.name

class Member(models.Model):
    club = models.ForeignKey(Club)
    student = models.ForeignKey(StudentProfile)
    admin = models.BooleanField(default = False)



class ClubFilter(django_filters.FilterSet):
    class Meta:
        model = Club
        fields = ['category']