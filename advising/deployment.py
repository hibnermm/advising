import os
from .settings import *

#warning during deployment
# https://django-secure.readthedocs.io/en/latest/settings.html#secure-hsts-seconds 
# https://www.toptal.com/django/secure-django-heroku-pydantic-tutorial-part-4
# ?: (security.W018) You should not have DEBUG set to True in deployment.
# ?: (security.W020) ALLOWED_HOSTS must not be empty in deployment.

#https://learn.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=flask%2Cwindows%2Cazure-cli%2Cvscode-deploy%2Cdeploy-instructions-azportal%2Cterminal-bash%2Cdeploy-instructions-zip-azcli

#made student account, followed directions best of ability:  https://advisingtool.azurewebsites.net/