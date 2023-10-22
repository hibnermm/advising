from django.db import models
from django import forms
from django.forms import ModelForm
from .models import Course

class CourseForm(ModelForm):
  class Meta: 
    model = Course
    fields = ('subj_abbrev', 'no', 'name', 'hours')
    """
    labels={
      'subj_abbrev': '',
      'no': forms.TextInput(attrs={'class':'form-control'}),
      'name': forms.TextInput(attrs={'class':'form-control'}),
      'hours': forms.TextInput(attrs={'class':'form-control'}),
    }
    """

    widgets = {
      'subj_abbrev': forms.TextInput(attrs={'class':'form-control'}),
      'no': forms.TextInput(attrs={'class':'form-control'}),
      'name': forms.TextInput(attrs={'class':'form-control'}),
      'hours': forms.TextInput(attrs={'class':'form-control'}),
    }



