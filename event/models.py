from django.db import models
from announcement.models import Announcement
import django_filters
from profiles.models import StudentProfile

TIME_FIELDS = (
        ('00','00:00'),
        ('01','01:00'),
        ('02','02:00'),
        ('03','03:00'),
        ('04','04:00'),
        ('05','05:00'),
        ('06','06:00'),
        ('07','07:00'),
        ('08','08:00'),
        ('09','09:00'),
        ('10','10:00'),
        ('11','11:00'),
        ('12','12:00'),
        ('13','13:00'),
        ('14','14:00'),
        ('15','15:00'),
        ('16','16:00'),
        ('17','17:00'),
        ('18','18:00'),
        ('19','19:00'),
        ('20','20:00'),
        ('21','21:00'),
        ('22','22:00'),
        ('23','23:00'),
               )

EVENT_CATEGORY = (('', 'All Events'),
                 ('1', 'Students\' Union Events'),
                 ('2', 'Sports Events'),
                 ('3', 'Academic Club Events'),
                 ('4', 'Cultural Activity Events'),
                 ('5', 'Career Events'),
                 ('6', 'Investment & Finance Events'),
                 ('7', 'Technology-related Events'),
                 ('8', 'Skill-building Events'),
                 ('9', 'Others'),
)

class Event(Announcement):
    title = models.CharField(max_length=40)
    date = models.DateField()
    start_time = models.CharField(max_length=2, choices=TIME_FIELDS)
    end_time = models.CharField(max_length=2, choices=TIME_FIELDS)
    venue = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True)
    registered = models.ManyToManyField(StudentProfile, blank=True)
    category = models.CharField(max_length=2, choices=EVENT_CATEGORY)
#    registration_link = models.URLField(verify_exists=True, blank=True)

    def __init__(self, *args, **kwargs):
        super(Event, self).__init__(*args, **kwargs)

    def __unicode__(self):
        return self.club + ' : ' + self.title
##        return self.club + " : " + self.title


class EventFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(lookup_type='lt')
    class Meta:
        model = Event
        fields = ['category', 'date']

#    def __init__(self, *args, **kwargs):
#        super(EventFilter, self).__init__(*args, **kwargs)
#        self.filters['category'].extra.update(
#            {'empty_label': u'All Categories'})

##def month_listing(request,yr,mm,dd):
##    yr1=int(yr)
##    mm1=int(mm)
##    dd1=int(dd)
##    eventdetail=Event.objects.filter(date=datetime.date(yr1,mm1,dd1))
##    return render_to_response('events/calendar.html',{'eventdetail':eventdetail},context_instance=RequestContext(request))
    
