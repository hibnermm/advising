from django.shortcuts import render
from checklist.models import Program, Course, ProgramCourses

# Create your views here.
def index(request):
  return render(request, "checklist/base.html")

def program_list(request):
  programs = Program.objects.all()
  courses = Course.objects.all()
  context = {'programs': programs, 'courses': courses}
  return render(request, 'checklist/program_list.html', context)

def program_search(request):
  programs = Program.objects.all()
  program_info =  [ ]
  for program in programs:
    courses = program.course_set.all()
    program_info.append({ 'programs': programs, 'course_set': course_set })
  context = {'program_info': program_info}
  return render(request, 'checklist/program_search.html', context)
