from django.contrib import admin
from checklist.models import Program, Course, ProgramCourses
from django import forms
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponseRedirect
# from django.urls import reverse
from checklist.resources import ProgramResource, CourseResource, ProgramCoursesResource
from import_export.admin import ImportExportModelAdmin  # ImportExportMixin
from django.template.response import TemplateResponse
from django.urls import path
from .forms import UploadFixture, CourseForm

#https://realpython.com/customize-django-admin-python/#overriding-django-admin-templates


# class csv_upload(forms.Form):
#     csv_upload = forms.FileField()


class ProgramAdmin(ImportExportModelAdmin):  # ImportExportMixin, admin.ModelAdmin
    resource_classes = [ProgramResource]
    list_display = ("level_abbrev", "major", "specialization")
    list_filter = ("level_abbrev", "major")


class CourseAdmin(ImportExportModelAdmin):  # admin.ModelAdmin, ImportExportModelAdmin)
    resource_classes = [CourseResource]
    list_display = ("subj_abbrev", "no", "name")
    list_filter = ("programs", "subj_abbrev")
    search_fields = ("no", "name")

    # def get_urls(self):
    #     urls = super().get_urls()
    #     new_urls = [
    #         path("upload/", self.upload),
    #     ]
    #     return new_urls + urls

    # def csv_upload(self, request):
    #     if request.method == "POST":
    #         csv_file = request.FILES["csv_upload"]

    #         if not csv_file.name.endswith(".csv"):
    #             messages.warning(request, "Error: Upload csv file.")
    #             return HttpResponseRedirect(request.path_info)

    #         file_data = csv_file.read().decode("utf-8")
    #         csv_data = file_data.split("\n")

    #         for c in csv_data:
    #             fields = c.split(",")
    #             created_course = course.objects.get_or_create(
    #                 subj_abbrev=row[0],
    #                 no=row[1],
    #                 name=row[2],
    #                 hours=row[3],
    #             )
    #         url = reverse("admin:index")
    #         return HttpResponseRedirect(url)
    #     form = CsvUpload()
    #     data = {"form": form}
    #     return render(request, "admin/csv_upload.html", data)


class ProgramCoursesAdmin(ImportExportModelAdmin):
    resource_classes = [ProgramCoursesResource]
    list_display = ("programs", "courses", "is_core", "is_degree", "is_major")
    list_filter = ("programs", "is_core", "is_degree", "is_major")
    search_fields = ("programs__major_abbrev", "programs__major")


# class ModelAdmin.add_view(request, form_url=', extra_context=None'):
#     pass

#https://docs.djangoproject.com/en/4.2/ref/contrib/admin/




class UploadFixture(admin.AdminSite):
    course_form = CourseForm
    
    def uploadfixture_view(self, request):
        request.checklist = self.name
        context = self.each_context(request)
        def get_urls(self):
            urls = super().get_urls()
            new_urls = [
                self.admin_view(path("upload-fixture/", self.upload_fixture, name="upload-fixture")),
            ]
            return base_urls + urlpatterns

    def upload_fixture(request):
        if request.method == "POST":
            form = UploadFixture(request.POST, request.FILES)
            # mimetype, encoding = mimetypes.guess_type(upload.name)
            # if mimetype != upload.content_type: raise TypeError("Type doesn't match file extension.")
            if form.is_valid(): #and isxlsx(file) or iscsv(file):
            # if not file.name.endswith(".json"):
            #     messages.warning(request, "Error: Upload json file.")
            #     return HttpResponseRedirect(request.path_info)
            
                url = reverse("admin/")
                return HttpResponseRedirect(url)
        else:
            form = UploadFixture()
        return render(request, "admin/upload_fixture.html", {"form": form}) 

        #can't get to display

# Register your models here.
admin.site.register(Program, ProgramAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(ProgramCourses, ProgramCoursesAdmin)
