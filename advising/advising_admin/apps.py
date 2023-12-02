from django.contrib.admin.apps import AppConfig


class AdvisingAdminConfig(AdminConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "advising_admin"
