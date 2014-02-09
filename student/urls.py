from django.conf.urls import patterns, url

from student import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^(?P<netid>\w{0,50})/$', views.detail, name='detail'),
)
