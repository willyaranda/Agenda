from django.conf.urls.defaults import *

urlpatterns = patterns('agenda.views',
    (r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', 'detail'),
)