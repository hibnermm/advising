from django.contrib import admin


class AdvisingAdminSite(admin.AdminSite):
    title_header = "Advising Admin"
    site_header = "Advising administration"
    index_title = "Advising site admin"
    change_template = "admin/checklist/change_list.html"