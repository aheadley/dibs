from django.conf.urls.defaults import *
from django.contrib import admin
from views import *
admin.autodiscover()

urlpatterns = patterns('ib.views',
    url(r'^(?:index/?)?$',
        index,
        name='index_view'),
    url(r'^(?P<board_slug>[A-Za-z0-9_-]+)/?$',
        board,
        name='board_view'),
    url(r'^(?P<board_slug>[A-Za-z0-9_-]+)/(?P<thread_id>\d+)/?$',
        thread,
        name='thread_view'),
)