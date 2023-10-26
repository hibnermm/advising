from django.urls import path
from . import views


urlpatterns = [
  path('program/', views.program_list, name='program-list'),
  path('search/', views.program_search, name='program-search'),
 # path('addcourse/', views.add_course, name='add-course'),
]
