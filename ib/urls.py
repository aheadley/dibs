from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('ib.views',
    (r'^(?:index/?)?$', 'index'),
    (r'^thread/(?P<thread_id>\d+)/?$', 'thread'),
)
