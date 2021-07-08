from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Course, Student, Teacher, CustomUser, adminUser
# Register your models here.

class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser, UserModel)
admin.site.register(adminUser)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Student)