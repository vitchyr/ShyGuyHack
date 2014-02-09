from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^instructor/', include('instructor.urls')),
    url(r'^courses/', include('courses.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
