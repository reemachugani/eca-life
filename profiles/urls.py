
from django.conf.urls.defaults import *

from ecalife.profiles import views
from ecalife.profiles.forms import ProfileForm
from django.contrib.auth import views as auth_views
from ecalife.profiles import avatar


urlpatterns = patterns('',
                       url(r'^create/$',
                           views.create_profile,
                           {'form_class': ProfileForm},
                           name='profiles_create_profile'),
                       url(r'^edit/$',
                           views.edit_profile,
                           {'form_class': ProfileForm},
                           name='profiles_edit_profile'),
                       url(r'^(?P<username>\w+)/$',
                           views.profile_detail,
                           name='profiles_profile_detail'),
                       url(r'^$',
                           views.profile_list,
                           name='profiles_profile_list'),
                       url(r'^password/change/$',
                           auth_views.password_change,
                               {'template_name': 'profiles/password_change.html'},
                           name='auth_password_change'),
                       url(r'^password/change/done/$',
                           auth_views.password_change_done,
                               {'template_name': 'profiles/password_change_done.html'},
                           name='auth_password_change_done'),
                       url(r'^change_avatar/$', views.add_avatar, name='change_avatar')
                       )
