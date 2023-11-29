from django.contrib import admin
from checklist.models import Program, Course, ProgramCourses
from django import forms
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


class csv_upload(forms.Form):
    csv_upload = forms.FileField()


class CourseAdmin(admin.ModelAdmin):
    list_display = ("subj_abbrev", "no", "name")
    list_filter = ("programs", "subj_abbrev")
    search_fields = ("no", "name")

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path("csv-upload/", self.csv_upload),
        ]
        return new_urls + urls

    def csv_upload(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]

            if not csv_file.name.endswith(".csv"):
                messages.warning(request, "Error: Upload csv file.")
                return HttpResponseRedirect(request.path_info)

            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for c in csv_data:
                fields = c.split(",")
                created_course = course.objects.get_or_create(
                    subj_abbrev=row[0],
                    no=row[1],
                    name=row[2],
                    hours=row[3],
                )
            url = reverse("admin:index")
            return HttpResponseRedirect(url)
        form = CsvUpload()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)


class ProgramAdmin(admin.ModelAdmin):
    list_display = ("level_abbrev", "major", "specialization")
    list_filter = ("level_abbrev", "major")


class ProgramCoursesAdmin(admin.ModelAdmin):
    list_display = ("programs", "courses", "is_core", "is_degree", "is_major")
    list_filter = ("programs", "is_core", "is_degree", "is_major")
    search_fields = ("programs__major_abbrev", "programs__major")


# Register your models here.
admin.site.register(Program, ProgramAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(ProgramCourses, ProgramCoursesAdmin)
