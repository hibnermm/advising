from django.contrib import admin
from django.contrib.admin.apps import AdminConfig
from django.template.response import TemplateResponse
from django.urls import path

# Register your models here.

class AdvisingAdmin(admin.AdminSite):
  title_header = "Advising Admin"
  site_header = "Advising Administration"
  index_title = "Advising site admin"

  #this isn't working...





"""

def upload( self, request):
  request.current_app = self.name
  context = self.each_context(request)
  return TemplateResponse(request, "admin/admin_upload", context)


def get_urls(self):
  urls = super().get_urls()
  url_patterns = [
    path("admin_upload", self.admin_view(self.))
  ]


"""