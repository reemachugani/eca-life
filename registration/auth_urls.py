
from django.conf.urls.defaults import patterns, url
from django.contrib.auth import views as auth_views
import registration

urlpatterns = patterns('',
    url(r'^login/$', auth_views.login, {'template_name': 'welcome.html'}, name='auth_login'),
    url(r'^logout/$', registration.views.logout_view, name='auth_logout'),
    url(r'^password/reset/$', auth_views.password_reset, {'template_name': 'registration/password_reset.html'}, name='auth_password_reset'),
    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm, {'template_name': 'registration/password_reset_confirm.html'}, name='auth_password_reset_confirm'),
    url(r'^password/reset/complete/$', auth_views.password_reset_complete, {'template_name': 'registration/password_reset_complete.html'}, name='auth_password_reset_complete'),
    url(r'^password/reset/done/$', auth_views.password_reset_done, {'template_name': 'registration/password_reset_done.html'}, name='auth_password_reset_done'),
)