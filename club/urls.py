from django.conf.urls.defaults import *
from club.views import *
from ecalife.event.views import *
from ecalife.forum.views import *
from ecalife.announcement.views import *
import search

urlpatterns = patterns('',
#    (r'^$', all_clubs),
    (r'^my_clubs/$', my_clubs),
    (r'^$', club_list),
    (r'^(\d+)/$', club_page),
    (r'^add_club/$', add_club),
    (r'^(\d+)/add_event/$', add_event),
    (r'^(\d+)/new_forum/$', new_forum),
    (r'^(\d+)/delete_forum/$', delete_forum),
    (r'^(\d+)/make_announcement/$', announce),
    (r'^(\d+)/become_member/$', become_member),
    (r'^(\d+)/all_announcements/$', club_wise_announce),
    (r'^(\d+)/all_events/$', club_wise_events),
    (r'^(\d+)/all_club_forums/$', club_wise_forums),

)