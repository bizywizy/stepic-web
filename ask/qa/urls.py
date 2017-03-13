from django.conf.urls import url

from .views import *

urlpatterns = [ 
    url(r'^$', index_page),
    url(r'^login/$', test),
    url(r'^signup/$', test),
    url(r'^question/(?P<pk>[0-9]+)/$', detail_page, name='detail'),
    url(r'^ask/$', test),
    url(r'^popular/$', popular_page),
    url(r'^new/$', test)
]
