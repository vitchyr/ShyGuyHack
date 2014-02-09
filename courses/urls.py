from django.conf.urls import patterns, url

from courses import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^create/$', views.create, name='create'),
  url(r'^(?P<course_id>\d+)/get_data$', views.get_data, name='get_data'),
  url(r'^vote/(?P<course_id>\d+)/$', views.vote, name='vote'),
  url(r'^(?P<course_id>\d+)/$', views.details, name='details'),
)
