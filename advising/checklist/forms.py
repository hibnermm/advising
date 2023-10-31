from django.db import models
from django import forms
from django.forms import ModelForm
from .models import Course, Program, ProgramCourses
#from django.views.generic.edit import CreateView

class CourseForm(ModelForm):
  class Meta: 
    model = Course
    fields = ('subj_abbrev', 'no', 'name', 'hours')


    
"""
class CourseCreateView(CreateView):        #not defined....mmmm
  model = Course
  fields = ['subj_abbrev', 'no', 'name', 'hours']
  template = 'add_course.html'
  success_url = 'success'

"""
class ProgramForm(ModelForm):
  class Meta:
    model = Program
    fields = ('level_abbrev', 'major', 'major_abbrev', 'specialization', 'spec_abbrev')

class ProgramCoursesForm(ModelForm):
  class Meta:
    model = ProgramCourses
    fields = ('programs', 'courses', 'is_core', 'is_degree', 'is_major', 'semester')


class UploadForm(models.Model):
  name = forms.TextInput()
  class Meta:
    model: Course
  file_upload = forms.FileField()


  #how to upload and import data into database https://www.youtube.com/watch?v=vs6dXL9Wp7s