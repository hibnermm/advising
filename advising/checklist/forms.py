from django.db import models
from django import forms
from django.forms import ModelForm
from .models import Course, Program, ProgramCourses
from django.core.exceptions import ValidationError

class CourseForm(ModelForm):
  class Meta: 
    model = Course
    fields = 'subj_abbrev', 'no', 'name', 'hours'

class ProgramForm(ModelForm):
  class Meta:
    model = Program
    fields = "__all__"
    #fields = ('level_abbrev', 'major', 'major_abbrev', 'specialization', 'spec_abbrev')

class ChecklistForm(ModelForm):
  class Meta:
    model = ProgramCourses
    fields = "__all__"
    #fields = ('programs', 'courses', 'is_core', 'is_degree', 'is_major', 'semester')


class UploadForm(forms.Form):
  course_csvfile = forms.FileField(required=False)
  program_csvfile = forms.FileField(required=False)
  checklist_csvfile = forms.FileField(required=False)
    

class SearchProgramForm(forms.Form):
  search_by = forms.ChoiceField(required=False, choices = (("level_abbrev", "Degree"), ("major", "Major"), ("specialization", "Specialization")))
  search = forms.CharField(required=False, min_length=2)

