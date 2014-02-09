from django.shortcuts import render, get_object_or_404

from django.shortcuts import render
from django.http import HttpResponse

from courses.models import Course, Tag

# Create your views here.
def index(request):
  return HttpResponse('test')

def create(request):
  c = Course(name='test course',description='test descript')
  c.save()
  return HttpResponse('Course created')

def details(request, course_id):
  c = get_object_or_404(Course, pk=course_id)
  netid = request.POST['netid']
  tags = request.POST['tags']
  t = Tag(course=c, name=netid, count=1)
  t.save()
  return HttpResponse(str(t))
