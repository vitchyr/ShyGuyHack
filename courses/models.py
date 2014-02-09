from django.db import models

class Course(models.Model):
  name = models.CharField(max_length=200)
  description = models.TextField()
  
  def __str__(self):
    return self.name

class Tag(models.Model):
  course = models.ForeignKey(Course)
  name = models.CharField(max_length=200)
  count = models.IntegerField()

  def __str__(self):
    return self.name
