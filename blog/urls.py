#coding:utf8
from django.conf.urls import patterns, url
from views import PostListView, PostDetailView

urlpatterns = patterns('',
                       url(r'^$', PostListView.as_view(),name='list'),
                       url(r'^(?P<pk>\d+)/$',PostDetailView.as_view()),
                      )