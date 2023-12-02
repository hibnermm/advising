# https://docs.djangoproject.com/en/1.10/howto/initial-data/#initial-data-via-fixtures
# https://docs.djangoproject.com/en/1.10/ref/django-admin/#django-admin-dumpdata
# https://docs.djangoproject.com/en/4.2/topics/db/fixtures/

# python manage.py or ? django-admin loaddata mydata.json


# write each json file by model...what do you do about many2many?
? is there a way to take a csv and convert to json? writing by hand seems like tedious
# - model: myapp.person
#   pk: 1
#   fields:
#     first_name: John
#     last_name: Lennon
# - model: myapp.person
#   pk: 2
#   fields:
#     first_name: Paul
#     last_name: McCartney


load multiple fixtures (models)
django-admin loaddata mammals birds insects
