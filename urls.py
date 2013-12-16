from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
        url(r'^$', RedirectView.as_view(url='/tasks/', permanent=False)),
        url(r'^tasks/', include('tasks.urls', namespace='tasks')),
        url(r'^admin/', include(admin.site.urls)),
        )
