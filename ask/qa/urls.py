from django.conf.urls import url, include
from django.contrib.auth.views import login
from .views import *

urlpatterns = [
    url(r'^$', index_page, name='index'),
    url(r'^login/$', login, {'template_name': 'qa/login.html'}, name='login'),
    url(r'^signup/$', signup_page, name='signup'),
    url(r'^question/(?P<pk>[0-9]+)/$', detail_page, name='detail'),
    url(r'^ask/$', ask_page, name='ask'),
    url(r'^popular/$', popular_page),
    url(r'^new/$', index_page)
]
