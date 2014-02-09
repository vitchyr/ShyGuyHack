from django.db import models
from courses.models import Course

# Create your models here.
class Student(models.Model):
  netid = models.CharField(max_length=200)
  courses = models.ManyToManyField(Course)
