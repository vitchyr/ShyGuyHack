import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from student.models import Student
from courses.models import Course

# Create your views here.
def index(request):
  return HttpResponse('student page')

def detail(request, netid):
  student = get_object_or_404(Student, netid=netid)
  courses = student.courses.all()
  course_names = []
  for c in courses:
    course_names.append(c.name)
  return HttpResponse(json.dumps(course_names))
