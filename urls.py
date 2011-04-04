from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    #Internacionalization
    #(r'^i18n/', include('django.conf.urls.i18n')),
    
    (r'^$', 'agenda.views.index'),
)

urlpatterns += patterns('agenda.views',
    (r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', 'detail'),
)