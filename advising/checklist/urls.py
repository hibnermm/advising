
from django.urls import path
from . import views


urlpatterns = [
  path('program/', views.program_list, name='program_list')
]