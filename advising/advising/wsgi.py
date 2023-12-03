"""
WSGI config for advising project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "advising.settings")
# os.environ.setdefault("DJANGO_CONFIGURATION", "Dev")

from django.core.wsgi import get_wsgi_application

# from configurations.management import execute_from_command_line

application = get_wsgi_application()
