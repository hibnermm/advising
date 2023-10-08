from django.contrib import admin
from .models import Subject, Course, Student, StudentCourses


# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(StudentCourses)