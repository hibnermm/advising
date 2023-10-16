from django.contrib import admin
from checklist.models import (Department, Subject, Field, TrainingLevel, Requirement, Course, Semester)

# Register your models here.
admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(Field)
admin.site.register(TrainingLevel)
admin.site.register(Requirement)
admin.site.register(Course)
admin.site.register(Semester)

"""
class FieldInLine(admin.TabularInline):
  model = Field

class TrainingLevel(admin.ModelAdmin):
  inlines = [
    FieldInLine,
  ] 

Thsi didn't work to link Field and TrainingLevel in same page...
how to put together two models so data entry is easiest when linking them?
"""