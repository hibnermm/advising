from django.shortcuts import render
from .models import Degree, Course, Requirement

# Create your views here.

def index(request):
  return render(request, "checklist/base.html")

def program_search(request):
  search_text = request.GET.get("search", " ")
  return render(request, "checklist/program_search.html", {"search_text": search_text}) 


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

  

