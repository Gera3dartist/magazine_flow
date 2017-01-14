from django.conf.urls import patterns, url, include
from reporter.views.user_info import GetInfoReporter
from .views.auth import AuthenticateReporterView, AuthLogoutReporterView

__author__ = 'agerasym'


auth_urls = patterns(
    '',
    url(r'^auth/login/?$', AuthenticateReporterView.as_view(), name='auth-login'),
    url(r'^auth/logout/?$', AuthLogoutReporterView.as_view(), name='auth-logout'),
    url(r'^profile/info/?$', GetInfoReporter.as_view(), name='info-profile'),
)


urlpatterns = patterns(
    '',
    '', include(auth_urls),
)