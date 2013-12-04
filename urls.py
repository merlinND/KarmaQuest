from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'site.views.home', name='home'),

    # Admin site
    url(r'^admin/', include(admin.site.urls)),
)
