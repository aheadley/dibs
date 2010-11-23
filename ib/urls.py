from django.conf.urls.defaults import *
from django.contrib import admin
from views import *
admin.autodiscover()

urlpatterns = patterns('ib.views',
    url(r'^(?:index/?)?$', 'index', name='board_index_view'),
    url(r'^thread/(?P<thread_id>\d+)/?$', 'thread', name='thread_view'),
)
