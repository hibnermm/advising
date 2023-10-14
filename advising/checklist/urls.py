
from django.urls import path
from . import views


urlpatterns = [
  path('degree/', views.degree_list, name = 'degree_list')
]
