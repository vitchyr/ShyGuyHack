from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^courses/', include('courses.urls')),
    url(r'^student/', include('student.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if not settings.DEBUG:
  urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
