from django.conf.urls import patterns, include, url

urlpatterns = patterns('tasks.views',
        url(r'^$', 'home_feed', name='home'),
        url(r'^all$', 'list_all_tasks', name='list_all_tasks'),
        )
