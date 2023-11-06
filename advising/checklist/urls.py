from django.urls import path
from . import views
#from .views import ProgramUploadView


urlpatterns = [
  path('course/', views.course_list, name='course-list'),
  path('program/', views.program_list, name='program-list'),
  path('search/', views.program_search, name='program-search'),
  path('addcourse/', views.add_course, name='add-course'),
  #path('addcourse', CourseCreateView.as_view(), name='add-course'),
  path('addprogram/', views.add_program, name='add-program'),
  path('linkcourseprogram/', views.link_course_program, name='link-course-program'),
  path('uploadprogram/', views.upload_program, name='upload-program')
  #path('uploadprogram/', ProgramUploadView.as_view(), name='upload-program'),
]
