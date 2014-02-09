from django.conf.urls import patterns, url

from student import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^(?P<netid>\w{0,200})/create$', views.create, name='create'),
  url(r'^(?P<netid>\w{0,200})/login$', views.login, name='login'),
  url(r'^signin/', views.signin, name='signin'),
  url(r'^(?P<netid>\w{0,200})/enroll$', views.enroll, name='enroll'),
  url(r'^(?P<netid>\w{0,200})/$', views.detail, name='detail'),
)
