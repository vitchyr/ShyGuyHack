import json

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from courses.models import Course, Tag

# Create your views here.
def index(request):
  courses = Course.objects.all()
  context = {
    'courses': courses,
  }
  return render(request, 'courses/index.html', context)

def create(request, course_name):
  exists = Course.objects.filter(name=course_name)
  if len(exists) > 0:
    return HttpResponse('Class already exists')
    
  try:
    des = request.GET['description']
  except:
    des = "Class for " + course_name
  c = Course(name=course_name,description=des)
  c.save()
  return HttpResponse('Course ' + c.name + ' created.')

def get_data(request, course_name):
  c = get_object_or_404(Course, name=course_name)
  course_tags = Tag.objects.filter(course=c.pk)
  tag_count = 0
  for t in course_tags:
    tag_count += t.count
  data = {"count": tag_count}
  output = json.dumps(data)
  return HttpResponse(output)

def get_tags(request, course_name):
  c = get_object_or_404(Course, name=course_name)
  raw_tags = Tag.objects.filter(course=c.pk)
  tags = []

  for t in raw_tags:
    d = {}
    d['name'] = t.name
    d['count'] = t.count
    tags.append(d)

  sorted_tags = sorted(tags, key=lambda k: k['count']) 
  output = json.dumps(sorted_tags)
  return HttpResponse(output)

# creates or increments a tag
def increment_tag(c, tag_text):
  tags = Tag.objects.filter(course=c, name=tag_text)
  if len(tags) == 0: # first of the tag
    t = Tag(course=c, name=tag_text, count=1)
  else:
    t = tags[0]
    t.count += 1
  t.save()

default_tag = "General Confusion"

def vote(request, course_name):
  c = get_object_or_404(Course, name=course_name)
  increment_tag(c, default_tag)
  return HttpResponse("Voted for class " + str(c.name))

# Add a tag to a course
def tag(request, course_name):
  c = get_object_or_404(Course, name=course_name)
  try:
    tag_text = request.GET['tag']
  except:
    tag_text = default_tag
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

# Professor clears a tag
def clear(request, course_name):
  try:
    tag_name = request.GET['tag']
  except:
    return HttpResponse("Cannot delete tag.")
  c = get_object_or_404(Course, name=course_name)
  Tag.objects.filter(course=c.pk, name=tag_name).delete()
  return HttpResponse("Tag deleted.")

def details(request, course_name):
  courses = Course.objects.filter(name=course_name)
  if len(courses) == 0:
    return HttpResponse('Course does not exist.')
  course = courses[0]
  tags = Tag.objects.filter(course=course.pk)

  context = {'course': course, 'tags': tags}
  return render(request, 'courses/instructor_view.html', context)
