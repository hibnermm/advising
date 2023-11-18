from django.contrib import admin
from checklist.models import Program, Course, ProgramCourses
from .forms import UploadForm



class CourseAdmin(admin.ModelAdmin):   #amin customizations to models
  list_display = ("subj_abbrev", "no", "name")
  list_filter = ("programs","subj_abbrev")
  search_fields = ("no", "name")
  #@admin.display(ordering="subj_abbrev",)  
  # error class ProgramAdmin(admin.ModelAdmin IndentationError: unexpected unindent>>

class ProgramAdmin(admin.ModelAdmin):
  list_display = ("level_abbrev", "major", "specialization")
  list_filter = ("level_abbrev", "major")
  

class ProgramCoursesAdmin(admin.ModelAdmin):
  list_display = ("programs", "courses", "is_core", "is_degree", "is_major")
  list_filter = ("programs",  "is_core", "is_degree", "is_major")
  search_fields = ("programs__major_abbrev", "programs__major")


class UploadFormAdmin(admin.ModelAdmin):
  form = UploadForm

# Register your models here.
admin.site.register(Program, ProgramAdmin)
#admin.site.register(Course), admin.site.register(CourseAdmin) need to add together
admin.site.register(Course, CourseAdmin)
admin.site.register(ProgramCourses, ProgramCoursesAdmin)
#admin.site.register(UploadFormAdmin) didn't work -> needs models to pull from?