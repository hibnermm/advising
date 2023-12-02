from checklist.models import Program, Course, ProgramCourses
from import_export import resources, fields, widgets
from import_export.widgets import ForeignKeyWidget, IntegerWidget, DecimalWidget
from import_export.fields import Field


class ProgramResource(resources.ModelResource):
    class Meta:
        model = Program
        # skip_unchanged = True
        # report_skipped = False
        # fields = ('id', "level_abbrev", "major", "specialization")


#         export_order = ('id', "level_abbrev", "major", "specialization")


class CourseResource(resources.ModelResource):
    # no = fields.Field(column_name='no', attribute='no', widget=DecimalWidget())  continues to show error conversion..
    # hours = fields.Field(column_name='hours', attribute='hours', widget=DecimalWidget())
    # no = fields.Field(column_name='no', attribute='no', widget=IntegerWidget())
    # hours = fields.Field(column_name='hours', attribute='hours', widget=IntegerWidget())
    # Field(attribute='no', widget=IntegerWidget(clean(value, row=None, **kwargs)))
    # programs = fields.Field(
    # column_name='programs',
    # attribute='programs',
    # widget=widgets.ManyToManyWidget(Program, field='id', separator='|')

    class Meta:
        model = Course
        # skip_unchanged = True
        # report_skipped = False
        # fields = ('id', 'subj_abbrev', 'no', 'name', 'hours')
        # export_order = ('id', 'subj_abbrev', 'no', 'name', 'hours')


# decimal.InvalidOperation: [<class 'decimal.ConversionSyntax'>]  -> This occurs and signals invalid-operation if a string is being converted to a number and it does not conform to the numeric string syntax. The result is [0,qNaN].
# https://stackoverflow.com/questions/64328619/how-to-format-export-fields-with-numeric-values-in-django-import-export
# https://django-import-export.readthedocs.io/en/latest/api_widgets.html#import_export.widgets.IntegerWidget.clean


class ProgramCoursesResource(resources.ModelResource):
    class Meta:
        model = ProgramCourses


# https://django-import-export.readthedocs.io/en/latest/getting_started.html#introduction
# https://adiramadhan17.medium.com/django-admin-export-to-excel-csv-and-others-94f8247304ba
