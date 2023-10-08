from django.shortcuts import render, get_object_or_404
from .models import Course, Student, Subject

# Create your views here.
def index(request):
  return render(request, "checklist/base.html")


def course_list(request):
  courses = Course.objects.all()
  courses.order_by('subject__subject_abbrev').values()
  context = {
        'courses': courses,
    }
  return render(request, 'checklist/course_list.html', context)

  """how to sort course by subject_abbrev?
  courses.order_by('subject__subject_abbrev')
  courses has fk of subject id, maybe set up model differently?
  """


  
def student_list(request):
  students = Student.objects.all()
  students.order_by('last_name').values()
  context = {
        'students': students,
    }
  return render(request, 'checklist/student_list.html', context)


"""
attempt: if student id has value, print coursework
difficulty figuring out how to set up model relationships in models.py and access those relations in views.py
  students = Student.objects.all()
  student_list = [ ]
  for student in students:
    courses = students.course_set.all()
    if student.school_id == True;
      student_list.append(
        {'course_number': course_number, 
        'course_name': course_name, 
        'credit_hours': credit_hours})

  context = {
    'student_list': student_list,
  }
  return render(request, "checklist/student_list.html", context)
  """


def subject_list(request):
  subjects = Subject.objects.all()
  subjects.order_by('subject_abbrev').values()
  context = {
        'subjects': subjects,
    }
  return render(request, 'checklist/subject_list.html', context)