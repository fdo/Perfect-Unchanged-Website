from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^mydjango/', include('mydjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^WebMaster/', include(admin.site.urls)),
    (r'^people/colors/$',  'mydjango.people.views.colors'),
    (r'^people/[a-z]/$',  'mydjango.people.views.colors'),
    (r'^people/[A-Z]/$',  'mydjango.Fitness.views.index'),
    (r'^people/', 'mydjango.people.views.index'),
    (r'^fitness/', 'mydjango.Fitness.views.index'),
    (r'^', 'mydjango.people.views.colors'),
)
