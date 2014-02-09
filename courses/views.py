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

# creates or increments a tag
def increment_tag(c, tag_text):
  tags = Tag.objects.filter(name=tag_text)
  if len(tags) == 0: # first of the tag
    t = Tag(course=c, name=tag_text, count=1)
  else:
    t = tags[0]
    t.count += 1
  t.save()

def vote(request, course_name):
  c = get_object_or_404(Course, name=course_name)
  default_tag = "default"
  increment_tag(c, default_tag)
  return HttpResponse("Voted for class " + str(c.name))

# Add a tag to a course
def tag(request, course_name):
  c = get_object_or_404(Course, name=course_name)
  tag_text = request.GET['tag']
  increment_tag(c, tag_text)
  return HttpResponse("Tag added")

# Get tags of a course
def tags(request, course_name):
  c = get_object_or_404(Course, name=course_name)
  tags = Tag.objects.filter(course=c.pk)
  tag_names = []
  for t in tags:
    tag_names.append(t.name)
  return HttpResponse(json.dumps(tag_names))
  
def details(request, course_name):
  context = {}
  return render(request, 'courses/instructor_view.html', context)

def get_data(request, course_name):
  print("get_data called")
  c = get_object_or_404(Course, name=course_name)
  course_tags = Tag.objects.filter(course=c.pk)
  tag_count = 0
  for t in course_tags:
    tag_count += 1
  data = {'count': tag_count}
  output = json.dumps(data)
  return output
