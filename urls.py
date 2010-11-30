from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^sams/', include('sams.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^WebMaster/', include(admin.site.urls)),
    (r'^people/colors/$',  'sams.people.views.colors'),
    (r'^people/[a-z]/$',  'sams.people.views.colors'),
    (r'^people/', 'sams.people.views.index'),
    (r'^fitness/', 'sams.Fitness.views.index'),
    (r'^', 'sams.people.views.colors'),
)