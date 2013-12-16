from django.conf.urls import patterns, include, url

urlpatterns = patterns('tasks.views',
        url(r'^$', 'home_feed', name='home_feed'),
        url(r'^all$', 'list_all_tasks', name='all_tasks'),
        )
