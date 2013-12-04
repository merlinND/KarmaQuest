from django.conf.urls import patterns, include, url

urlpatterns = patterns('tasks.views',
    url(r'^$', 'home', name='home'),
)
