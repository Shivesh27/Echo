from django.contrib import admin
from .models import Course, Teacher, PendingUsers, Student
# Register your models here.

admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(PendingUsers)
admin.site.register(Student)