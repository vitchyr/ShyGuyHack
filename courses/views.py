import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from courses.models import Course, Tag

# Create your views here.
def index(request):
  return HttpResponse('test')

def create(request):
  c = Course(name='test course',description='test descript')
  c.save()
  return HttpResponse('Course created with id = ' + str(c.pk))

def vote(request, course_name):
  c = get_object_or_404(Course, name=course_name)
  #netid = request.POST['netid']
  netid="vhp22"
  pop = 5
  #tags = request.POST['tags']
  t = Tag(course=c, name=netid, count=pop)
  t.save()
  return HttpResponse(str(t))

def details(request, course_name):
  context = {}
  return render(request, 'courses/instructor_view.html', context)

def get_data(request, course_name):
  #course_name = request.POST['course_name']
  #course_name = 1
  print("get_data called")
  c = Course.objects.filter(name=course_name)[0]
  course_tags = Tag.objects.filter(course=c.pk)
  tag_count = 0
  for t in course_tags:
    tag_count += 1
  data = {'count': tag_count}
  output = json.dumps(data)
  return output
