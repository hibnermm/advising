import os
from .settings import *

#warning during deployment
# https://django-secure.readthedocs.io/en/latest/settings.html#secure-hsts-seconds 
# https://www.toptal.com/django/secure-django-heroku-pydantic-tutorial-part-4
# ?: (security.W018) You should not have DEBUG set to True in deployment.
# ?: (security.W020) ALLOWED_HOSTS must not be empty in deployment.

#https://learn.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=flask%2Cwindows%2Cazure-cli%2Cvscode-deploy%2Cdeploy-instructions-azportal%2Cterminal-bash%2Cdeploy-instructions-zip-azcli

#made student account, followed directions best of ability:  https://advisingtool.azurewebsites.net/
# indicated web-app is running, not sure 



#under branch gh-pages, went to settings, then pages ->  https://hibnermm.github.io/advising/
# can only see readme....
# https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site


# https://www.benchatronics.com/detail/How-to-set-allowed-host-in-django
# If you are on development leave Debug=True
# On production set Debug = False
# On development put only the domains you want the site to be accessible with ['localhost', '127.0.0.1', '*']
# On production only put the domains that you configured your host with ['localhost', '127.0.0.1', 'yourdomain.com']


# https://www.w3schools.com/django/django_deploy_requirements.php
