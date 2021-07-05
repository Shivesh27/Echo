from django.db import models

# Create your models here.

class Course(models.Model):
	courseid = models.IntegerField()
	coursename = models.CharField(max_length = 20)
		
class Teacher(models.Model):
	teacherid = models.IntegerField()
	name = models.CharField(max_length = 50)
	email = models.EmailField()
	courses = models.ManyToManyField(Course)

class Student(models.Model):
	studentid = models.IntegerField()
	name = models.CharField(max_length = 50)
	email = models.EmailField()
	courses = models.ForeignKey(Course, on_delete = models.CASCADE)
