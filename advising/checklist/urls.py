from django.urls import path
from . import views


urlpatterns = [
  path('courses/', views.course_list, name='course_list'), 
  path('students/', views.student_list, name='student_list'),
  path('subjects/', views.subject_list, name='subject_list')
]
