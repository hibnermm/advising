from django.contrib import admin

class ChecklistAdminSite(admin.AdminSite):
    title_header = 'Checklist Admin'
    site_header = 'Checklist administration'
    index_title = 'Checklist site admin'