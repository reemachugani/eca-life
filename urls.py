from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from ecalife import settings, views
from django.contrib import admin
from ecalife.profiles.forms import ProfileForm
from ecalife.announcement.views import homepage
from django.contrib.auth import views as auth_views
from ecalife.search.views import search



admin.autodiscover()

urlpatterns = patterns('',
        (r'^admin/jsi18n', 'django.views.i18n.javascript_catalog'),
        (r'^admin/', include(admin.site.urls)),
        (r'^avatar/', include('avatar.urls')),
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
)
urlpatterns += patterns('',
        (r'^$', auth_views.login, {'template_name': 'welcome.html'}),
        (r'^homepage/$', homepage),
        (r'^search/$', search),
#        (r'^(?P<field>\w+)/filter/$', filter),
        url(r'^profiles/edit/$', 'profiles.views.edit_profile', {'form_class': ProfileForm,}),
        (r'^profiles/', include('profiles.urls')),
    )

urlpatterns += patterns('',
        (r'^accounts/', include('registration.urls')),
        (r'^clubs/', include('club.urls')),
        (r'^announcements/', include('announcement.urls')),
        (r'^events/', include('event.urls')),
        (r'^forums/', include('forum.urls')),
        (r'^messages/', include('messages.urls')),
        (r'^calendar/',include('eventcal.urls')),
        (r'^events/(?P<yr>\d{4})/(?P<mm>\d{2})/(?P<dd>\d{2})/$','ecalife.event.views.month_listing'),
    )

##
##urlpatterns += patterns('',
##        (r'^photologue/', include('photologue.urls')),
##    )
