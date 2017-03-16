from django.conf.urls import url, include
from django.contrib.auth.views import login, logout
from .views import *

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^login/$', login, {'template_name': 'qa/login.html'}, name='login'),
    url(r'^signup/$', SignupView.as_view(), name='signup'),
    url(r'^question/(?P<pk>[0-9]+)/$', AnswersView.as_view(), name='detail'),
    url(r'^ask/$', AskView.as_view(), name='ask'),
    url(r'^popular/$', PopularView.as_view(), name='popular'),
    url(r'^new/$', IndexView.as_view()),
    url(r'^logout/$', logout, name='logout')
]
