from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'phantom.views.home', name='home'),
    url(r'^checkpass/$', 'phantom.views.checkpassword'),


    url(r'^admin/', include(admin.site.urls)),
)
