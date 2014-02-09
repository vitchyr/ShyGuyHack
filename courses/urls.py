from django.conf.urls import patterns, url

from courses import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^(?P<course_name>\w{0,200})/create$', views.create, name='create'),
  url(r'^(?P<course_name>\w{0,200})/get_data$', views.get_data, name='get_data'),
  url(r'^(?P<course_name>\w{0,200})/get_tags$', views.get_tags, name='get_tags'),
  url(r'^(?P<course_name>\w{0,200})/vote$', views.vote, name='vote'),
  url(r'^(?P<course_name>\w{0,200})/tag$', views.tag, name='tag'),
  url(r'^(?P<course_name>\w{0,200})/tags$', views.tags, name='tags'),
  url(r'^(?P<course_name>\w{0,200})/clear$', views.clear, name='clear'),
  url(r'^(?P<course_name>\w{0,200})/$', views.details, name='details'),
)
