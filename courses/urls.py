from django.conf.urls import patterns, url

from courses import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^create/$', views.create, name='create'),
  url(r'^(?P<course_name>\w{0,50})/get_data$', views.get_data, name='get_data'),
  url(r'^(?P<course_name>\w{0,50})/vote$', views.vote, name='vote'),
  url(r'^(?P<course_name>\w{0,50})/tag$', views.tag, name='tag'),
  url(r'^(?P<course_name>\w{0,50})/tags$', views.tags, name='tags'),
  url(r'^(?P<course_name>\w{0,50})/$', views.details, name='details'),
)
