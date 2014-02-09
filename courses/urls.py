from django.conf.urls import patterns, url

from courses import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^create/$', views.create, name='create'),
  url(r'^get_data/$', views.get_data, name='get_data'),
  url(r'^(?P<course_id>\d+)/$', views.details, name='details'),
)
