from django.conf.urls.defaults import *
from announcement.views import *

urlpatterns = patterns('',
    (r'^my_clubs/$', myclub_announce),
)