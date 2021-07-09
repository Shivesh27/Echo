from django.db import models
from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUser(AbstractUser):
	user_data = (("1","admin"),("2","staff"),("3","student"))
	user_type = models.CharField(default="1",choices=user_data,max_length=10)

class adminUser(models.Model):
	user_id = models.OneToOneField(CustomUser,on_delete=models.CASCADE)

# Create your models here.
class Course(models.Model):
	courseid = models.IntegerField()
	coursename = models.CharField(max_length = 20)

class Teacher(models.Model):
	user_id = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
	teacherid = models.CharField(max_length = 10)
	courses = models.ManyToManyField(Course)

class Student(models.Model):
	user_id = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
	studentid = models.IntegerField()
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

@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
	if created:
		if instance.user_type== "1":
			adminUser.objects.create(user_id=instance)
		if instance.user_type== "2":
			Teacher.objects.create(user_id=instance)
		if instance.user_type== "3":
			Student.objects.create(user_id=instance)

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
	if instance.user_type == "1":
		instance.adminuser.save()
	if instance.user_type == "2":
		instance.teacher.save()
	if instance.user_type == "3":
		instance.student.save()
