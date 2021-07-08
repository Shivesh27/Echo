from django.db import models
from PIL import Image
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
	courses = models.ManyToManyField(Course)

class PendingUsers(models.Model):
	MALE = 'M'
	FEMALE = 'F'
	GENDER_CHOICES = (
		(MALE,'Male'),
		(FEMALE,'Female'))
	name = models.CharField(max_length = 50)
	email = models.EmailField()
	gender = models.CharField(max_length = 1,choices = GENDER_CHOICES, blank = True)
	collegeid = models.CharField(max_length = 5)
	enrollmentnumber = models.CharField(max_length = 10)
	yearofjoin = models.IntegerField()
	contact = models.CharField(max_length = 10, blank = True)
	idproof = models.ImageField(upload_to = 'id_pics')
	REQUIRED = ['name', 'email', 'collegeid', 'enrollmentnumber', 'yearofjoin', 'idproof']
	