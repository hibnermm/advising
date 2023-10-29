from django.db import models
from django import forms
from django.forms import ModelForm
from .models import Course, Program, ProgramCourses

class CourseForm(ModelForm):
  class Meta: 
    model = Course
    fields = ('subj_abbrev', 'no', 'name', 'hours')

class ProgramForm(ModelForm):
  class Meta:
    model = Program
    fields = ('level_abbrev', 'major', 'major_abbrev', 'specialization', 'spec_abbrev')

class ProgramCoursesForm(ModelForm):
  class Meta:
    model = ProgramCourses
    fields = ('programs', 'courses', 'is_core', 'is_degree', 'is_major', 'semester')