from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^api/', include('api.urls')),
    url(r'^bankprocess/', include('bankprocess.urls')),
    url(r'^admin/', include(admin.site.urls)),
)