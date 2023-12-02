from django.db import models
from django import forms
from django.forms import ModelForm
from .models import Course, Program, ProgramCourses
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class InstanceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        if kwargs.get("instance"):
            button_title = "Save"
        else:
            button_title = "Create"
        self.helper.add_input(Submit("", button_title))


class CourseForm(InstanceForm):
    class Meta:
        model = Course
        fields = "subj_abbrev", "no", "name", "hours"


class ProgramForm(InstanceForm):
    class Meta:
        model = Program
        fields = "__all__"
        # fields = ('level_abbrev', 'major', 'major_abbrev', 'specialization', 'spec_abbrev')


class ChecklistForm(ModelForm):
    class Meta:
        model = ProgramCourses
        fields = "__all__"
        # fields = ('programs', 'courses', 'is_core', 'is_degree', 'is_major', 'semester')


class UploadFixture(forms.Form):
    title = title = forms.CharField(max_length=50)
    date = forms.DateField()
    file = forms.FileField(required=False)


#     chap 8 web dev djnago
# class ExampleModel(models.Model):
#     file_field =
#     models.FileField(upload_to="files/%Y/%m/%d/")
# ? models.FF vs. forms.FF


class SearchProgramForm(forms.Form):
    search_by = forms.ChoiceField(
        required=False,
        choices=(
            ("level_abbrev", "Degree"),
            ("major", "Major"),
            ("specialization", "Specialization"),
        ),
    )
    search = forms.CharField(required=False, min_length=2)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "get"
        self.helper.add_input(Submit("", "Search"))
