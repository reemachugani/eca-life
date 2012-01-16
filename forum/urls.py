from django.conf.urls.defaults import *
from forum.models import *

urlpatterns = patterns('forum.views',
    (r'^(\d+)/$', "forum"),
    (r'^delete_forum/(\d+)/$', "delete_forum"),
    (r'^thread/id=(\d+)/$', "thread"),
    (r'^new_thread/(\d+)/$', "new_thread"),
    (r'^thread/edit/(?P<pk_thread>\d+)/(?P<pk_post>\d+)/$', "edit_post"),
    (r'^thread/delete/(?P<pk_thread>\d+)/(?P<pk_post>\d+)/$', "delete_post"),
    (r'', "main"),
)
