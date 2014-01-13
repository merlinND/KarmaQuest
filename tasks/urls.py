from django.conf.urls import patterns, include, url

urlpatterns = patterns('tasks.views',
        url(r'^$', 'list_all_tasks', name='all_tasks'),
        url(r'^feed$', 'home_feed', name='home_feed'),
        url(r'^(?P<task_id>\d+)/detail$', 'task_detail', name='task_detail'),

        #url(r'^$org/', 'list_all_organizations', name='all_organizations'),
        url(r'^org/(?P<org_id>\d+)/detail/*$', 'org_detail', name='org_detail'),
        url(r'^org/(?P<org_id>\d+)/tasks/*$', 'org_tasks', name='org_tasks'),
        )
