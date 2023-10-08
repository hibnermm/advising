from django.shortcuts import render
#from .models import modelName

# Create your views here.
def index(request):
  return render(request, "checklist/base.html")


