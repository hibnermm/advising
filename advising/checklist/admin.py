from django.contrib import admin
from checklist.models import Program, Course, ProgramCourses

"""
class CourseAdmin(admin.ModelAdmin):
  list_display = ("subj_abbrev", "no", "name")
  list_filter = ("subj_abbrev")
"""

# Register your models here.
admin.site.register(Program)
admin.site.register(Course)
admin.site.register(ProgramCourses)