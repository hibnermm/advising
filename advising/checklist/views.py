from django.shortcuts import render
from .models import Degree, Field #?

# Create your views here.
def index(request):
  return render(request, "checklist/base.html")

def degree_search(request):
  search_text = request.GET.get("search", " ")
  return render(request, "checklist/degree_search.html", {"search_text": search_text})     #not working

def degree_list(request):
  degrees = Degree.objects.all().order_by("degree_abbrev")
  fields = Degree.objects.prefetch_related('field')  #get field table for every item in degree query set; only shows BBA
  #departments = Department.objects.all()  no data
  context = {
        'degrees': degrees,
        'fields': fields,
        #'departments': departments
    }
  return render(request, 'checklist/degree_list.html', context)
