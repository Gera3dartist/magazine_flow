"""magazine_flow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from moderator.views import AuthenticateModeratorView, AuthLogoutModeratorView, BlogPostModeratorListView
from reporter.views.auth import AuthenticateReporterView, AuthLogoutReporterView
from reporter.views.blogpost import BlogPostListView, BlogPostListPublicView
from reporter.views.user_info import GetInfoReporter
from core.routers import CoreRoute

router = CoreRoute()
router.register(r'blogpost', BlogPostListView, base_name='orders')


m_router = CoreRoute()
m_router.register(r'blogpost', BlogPostModeratorListView, base_name='orders')


public_router = CoreRoute()
public_router.register(r'blogpost', BlogPostListPublicView, base_name='public')


reporter_patterns = patterns(
    '',
    url(r'^auth/login/?$', AuthenticateReporterView.as_view(), name='auth-login'),
    url(r'^auth/logout/?$', AuthLogoutReporterView.as_view(), name='auth-logout'),
    url(r'^profile/info/?$', GetInfoReporter.as_view(), name='auth-logout'),
    url(r'', include(router.get_urls())),
)

moderator_patterns = patterns(
    '',
    url(r'^auth/login/?$', AuthenticateModeratorView.as_view(), name='auth-login'),
    url(r'^auth/logout/?$', AuthLogoutModeratorView.as_view(), name='auth-logout'),
    url(r'', include(m_router.get_urls())),
)


api_patterns = patterns(
    '',
    url(r'^reporter/', include(reporter_patterns)),
    url(r'^moderator/', include(moderator_patterns)),
    url(r'^public/', include(public_router.get_urls())),
)


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(api_patterns)),

)
