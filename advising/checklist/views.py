from django.shortcuts import render
#from .models import modelName

# Create your views here.
def index(request):
  return render(request, "checklist/base.html")

def search(request):
  search_text = request.GET.get("search", " ")
  return render(request, "checklist/search.html", {"search_text": search_text})

