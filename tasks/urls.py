from django.conf.urls import patterns, include, url

urlpatterns = patterns('tasks.views',
        url(r'^$', 'list_all_tasks', name='all_tasks'),
        url(r'^feed$', 'home_feed', name='home_feed'),
        url(r'^(?P<task_id>\d+)/detail$', 'task_detail', name='task_detail'),
        )
