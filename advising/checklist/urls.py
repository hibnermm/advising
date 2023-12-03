from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from checklist.views import CourseListView


urlpatterns = [
    path("search", views.program_search, name="program-search"),
    path("program/", views.program_list, name="program-list"),
    path("program/<int:pk>", views.program_detail, name="program-detail"),
    # path('course/', views.course_list, name='course-list'),
    path("course/", CourseListView.as_view(), name="course-list"),
    path("course/<int:pk>", views.course_detail, name="course-detail"),
    path("courses/<int:pk>", views.course_edit, name="course-edit"),
    path("courses/new", views.course_edit, name="course-new"),
    path("checklist/", views.checklist_list, name="checklist-list"),
    path("checklists/<int:pk>", views.checklist_edit, name="checklist-edit"),
    path("checklists/<int:pk>", views.checklist_edit, name="checklist-new"),
    path("programs/<int:pk>", views.program_edit, name="program-edit"),
    path("programs/new", views.program_edit, name="program-new"),
    # path("upload/", views.upload_checklist, name="upload-checklist"),
    path("courses-pdf/", views.courses_pdf, name="courses-pdf"),
    path("courses-csv/", views.courses_csv, name="courses-csv"),
    path('dashboard', views.dashboard, name='dashboard')
    # path("pdf/", views.checklist_pdf, name="checklist-pdf")   "pdf/<int:pk>" didn't work for specific program -> specific checklist pdfs, do this later
]
