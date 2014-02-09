import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from student.models import Student
from courses.models import Course

# Create your views here.
def index(request):
  return HttpResponse('student page')

def get_course_names(student):
  courses = student.courses.all()
  course_names = []
  for c in courses:
    course_names.append(c.name)
  return course_names
  
def detail(request, netid):
  students = Student.objects.filter(netid=netid)
  if len(students) == 0:
    return HttpResponse("Student does not exist")
  
  student = students[0]
  course_names = get_course_names(student)
  return HttpResponse(json.dumps(course_names))

def create(request, netid):
  s = Student(netid=netid)
  s.save()
  return HttpResponse('Created!')

def login(request, netid):
  students = Student.objects.filter(netid=netid)
  if len(students) == 0:
    return HttpResponse("") # current protocol: return empty str if no student
  
  course_names = get_course_names(students[0])
  return HttpResponse(json.dumps(course_names))

def enroll(request, netid):
  try:
    course_name = request.GET['course']
  except:
    return HttpResponse("Please provide a course to enroll in.")

  courses = Course.objects.filter(name=course_name)
  if len(courses) == 0:
    return HttpResponse("No course called " + course_name + " exists")
  course = courses[0]

  students = Student.objects.filter(netid=netid)
  if len(students) == 0:
    student = Student(netid=netid)
  else:
    student = students[0]

  if course.student_set.filter(pk=student.pk).exists():
    return HttpResponse("Already enrolled")
    
  student.courses.add(course) 
  student.save()
  return HttpResponse("Enrolled in " + course.name)
