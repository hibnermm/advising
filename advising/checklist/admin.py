from django.contrib import admin
from checklist.models import(Degree, Requirement, Course, ProgramCourses, Prerequisite)


class CourseAdmin(admin.ModelAdmin):
  list_display = ("subj_abbrev", "no", "name")
  list_filter = ("subj_abbrev")




# Register your models here.
admin.site.register(Degree)
admin.site.register(Requirement)
admin.site.register(Course)
admin.site.register(ProgramCourses)
admin.site.register(Prerequisite)

