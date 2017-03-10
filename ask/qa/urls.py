from django.conf.urls import url

from .views import *

urlpatterns = [ 
    url(r'^$', test),
    url(r'^login/$', test),
    url(r'^question/(?P<pk>[0-9]+)/$', test),
    url(r'^ask/$', test),
    url(r'^popular/$', test),
    url(r'^new/$', test)
]
