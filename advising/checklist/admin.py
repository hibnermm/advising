from django.contrib import admin
from checklist.models import Program, Course, ProgramCourses



class CourseAdmin(admin.ModelAdmin): 
  list_display = ("subj_abbrev", "no", "name")
  list_filter = ("programs","subj_abbrev")
  search_fields = ("no", "name")



class ProgramAdmin(admin.ModelAdmin):
  list_display = ("level_abbrev", "major", "specialization")
  list_filter = ("level_abbrev", "major")
  

class ProgramCoursesAdmin(admin.ModelAdmin):
  list_display = ("programs", "courses", "is_core", "is_degree", "is_major")
  list_filter = ("programs",  "is_core", "is_degree", "is_major")
  search_fields = ("programs__major_abbrev", "programs__major")


# Register your models here.
admin.site.register(Program, ProgramAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(ProgramCourses, ProgramCoursesAdmin)
