from django.shortcuts import render
from .models import Department, Field, TrainingLevel

# Create your views here.
def index(request):
  return render(request, "checklist/base.html")

def degree_search(request):
  search_text = request.GET.get("search", " ")
  return render(request, "checklist/degree_search.html", {"search_text": search_text})     #not working

def degree_list(request):
  trainings= TrainingLevel.objects.all()
  fields = Field.objects.all()
  """not working, error undobunc local error, can't access courses
  for course in courses:
    courses = Course.objects.all()
    course_list = [ ]
    prereq = course.prereq_set.all()
    course_list.append({'course': course, 
                        'prereq': prereq})
"""
  context = {
        'trainings': trainings,
        'fields': fields,
        #'course_list': course_list
    }
  return render(request, 'checklist/degree_list.html', context)

"""
?How to access data if no FK on model?
field = Field.objects.all()
field.get(name__contains="computer")   #where %like%
field.filter(dept__name="Department of Life, Earth and Environmental Sciences")   #spans relationships, need to name FK model as on primary model
field.filter(traininglevels__abbrev="BBA")    #works

course.get.selectrelated().get(prereqs).values()  #doesn't work
courses.prereqs.all() #doesn't work, no attribute named 'prereq'
"""