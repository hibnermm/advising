from django.shortcuts import render
from .models import Degree, Course, Requirement, Prerequisite
from .forms import CourseForm
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
  return render(request, "checklist/base.html")


def program_list(request):
  degrees = Degree.objects.all()
  courses = Course.objects.all()
  requirements = Requirement.objects.all()
  context = {
    'degrees': degrees,
    'courses': courses,
    'requirements': requirements
          }
  return render(request, 'checklist/program_list.html', context)

  
def add_course(request):
  submitted = False
  if request.method == "POST":
    form = CourseForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/add_course?submitted=True')
  else: 
    form = CourseForm
    if 'submitted' in request.GET:
      submitted = True
  return render(request, "checklist/add_course.html", {'form': form, 'submitted': submitted})


def program_search(request):

  """   -> AttributeError: 'Course' object has no attribute 'reqs_set'
  degrees = Degree.objects.all()
  courses = Course.objects.all()
  progcourses = [ ]

  for course in courses:
    requirements = course.reqs_set.all()
    programcourses.append({'course': course, 'req': req})

  context = {
    'degrees': degrees,
    'progcourses': progcourses
          }

          """
  degrees = Degree.objects.all()
  courses = Course.objects.all()  
  requirements = Requirement.objects.all().prefetch_related('courses')
  prerequisites = Prerequisite.objects.select_related('course').all()  
    course_list.append({
      'course': course,
      'requirements': requirements,
      'prerequisites': prerequisites,
    })
  


  context = {
    'degrees': degrees,
    'course_list': course_list,

          }
  return render(request, 'checklist/program_search.html', context)

"""

  #courses = Course.objects.prefetch_related('reqs').all()  
  #links courses to requirements
  #<QuerySet [<Prerequisite: CIDM 1315: Programming Fundamentals>]>


 requirements = Requirement.objects.select_related().all()
 //didn't work


  sort_by = request.GET.get('sort_by')
  if sort_by == 'requirement':
    requirements = requirements.order_by('req')
  elif sort_by == 'course':
    courses = courses.order_by('subj_abbrev')
  elif sort_by == 'prerequisite': 
    prerequisites = prerequisites.order_by('subj_abbrev')
    """