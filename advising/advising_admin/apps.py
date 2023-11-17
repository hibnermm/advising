from django.contrib.admin.apps import AdminConfig


class AdvisingAdminConfig(AdminConfig):
    default_site = 'advising_admin.admin.AdvisingAdmin'


