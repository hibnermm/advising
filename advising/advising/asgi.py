"""
ASGI config for advising project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "advising.settings")
# os.environ.setdefault("DJANGO_CONFIGURATION", "DEV")

from django.core.asgi import get_asgi_application


# from configurations.asgi import get_asgi_application  
# doesn't work for django-configurations wip

application = get_asgi_application()
