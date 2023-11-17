from django.contrib import admin
from checklist.models import Program, Course, ProgramCourses
from .forms import UploadForm

"""
class CourseAdmin(admin.ModelAdmin):
  list_display = ("subj_abbrev", "no", "name")
  list_filter = ("subj_abbrev")
"""

class UploadFormAdmin(admin.ModelAdmin):
  form = UploadForm



# Register your models here.
admin.site.register(Program)
admin.site.register(Course)
admin.site.register(ProgramCourses)
#admin.site.register(UploadFormAdmin) didn't work