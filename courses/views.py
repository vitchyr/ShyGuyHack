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

def vote(request, course_id):
  c = get_object_or_404(Course, pk=course_id)
  #netid = request.POST['netid']
  netid="vhp22"
  pop = 5
  #tags = request.POST['tags']
  t = Tag(course=c, name=netid, count=pop)
  t.save()
  return HttpResponse(str(t))

def details(request, course_id):
  context = {}
  return render(request, 'courses/instructor_view.html', context)

def get_data(request, course_id):
  #course_id = request.POST['course_id']
  #course_id = 1
  print("get_data called")
  course_tags = Tag.objects.filter(course=course_id)
  tag_count = 0
  for t in course_tags:
    tag_count += 1
  data = {'count': tag_count}
  output = json.dumps(data)
  return HttpResponse(output)
