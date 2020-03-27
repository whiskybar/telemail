from django.conf.urls import patterns, include, url
from django.dispatch import receiver
from django.contrib import admin, auth
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/password_reset/$', 'django.contrib.auth.views.password_reset', name='admin_password_reset'),
    url(r'^admin/password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    url(r'^admin/', include(admin.site.urls)),
)

@receiver(auth.user_logged_in)
def strip_permissions(sender, request, user, **kwargs):
    # Check if the logged in user is admin@domain
    if not user.username.startswith('admin@'):
        return

    # Fetch the permissions to remove
    to_remove = user.user_permissions.filter(content_type__app_label__in=['auth', 'admin', 'contenttypes', 'sessions'])
    if not to_remove:
        return

    user.user_permissions.remove(*to_remove)
