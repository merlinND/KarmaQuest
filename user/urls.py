from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

urlpatterns = patterns('user.views',
        url(r'^$', RedirectView.as_view(url='profile', permanent=False)),
        url(r'^profile$', 'user_profile', name='user_profile')
        )
