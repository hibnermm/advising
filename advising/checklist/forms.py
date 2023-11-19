from django.db import models
from django import forms
from django.forms import ModelForm
from .models import Course, Program, ProgramCourses
#from django.views.generic.edit import CreateView

class CourseForm(ModelForm):
  class Meta: 
    model = Course
    fields = "__all__"
    #fields = ('subj_abbrev', 'no', 'name', 'hours') doesnt automatically connect programs

    
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
    fields = "__all__"
    #fields = ('level_abbrev', 'major', 'major_abbrev', 'specialization', 'spec_abbrev')

class ProgramCoursesForm(ModelForm):
  class Meta:
    model = ProgramCourses
    fields = "__all__"
    #fields = ('programs', 'courses', 'is_core', 'is_degree', 'is_major', 'semester')


class UploadForm(forms.Form):
  file_upload = forms.FileField()



class ProgramInfoForm(forms.Form):
  search = forms.CharField(required=False, min_length=2)
  search_by = forms.ChoiceField(required=False, choices = (("level_abbrev", "Degree"), ("major", "Major"), ("specialization", "Specialization")))

"""

class LoginForm(forms.Form):
  username = forms.CharField(max_length=100)
  password = forms.CharField(min_length=8, widget=forms.PasswordInput)
  hidden_input = forms.CharField(widget=forms.HiddenInput, initial="Hidden Value")

  """

