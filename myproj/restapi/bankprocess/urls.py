from django.conf.urls import patterns, url

urlpatterns = patterns(
    'bankprocess.views',
    # url(r'^tasks/$', 'task_list', name='task_list'),
    url(r'^customer/(?P<username>[^/]+)/(?P<password>[^/]+)/$', 'user_details', name='user_details'),
    url(r'^trans/(?P<pk>[^/]+)/$', 'list_transaction', name='list_transaction'),  
   	
    # url(r'^tasks/$', 'task_list', name='task_list'),
    # url(r'^tasks/(?P<pk>[0-9]+)$', 'task_detail', name='task_detail'),
)