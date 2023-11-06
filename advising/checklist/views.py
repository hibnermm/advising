from django.shortcuts import render, get_object_or_404
from django.conf import settings
from checklist.models import Program, Course, ProgramCourses
from checklist.forms import CourseForm, ProgramForm, ProgramCoursesForm, UploadForm
from django.http import HttpResponseRedirect
from django.views import View
import io, csv



# Create your views here.
def index(request):
  return render(request, "checklist/base.html")

def course_list(request):
  courses = Course.objects.all()
  context = {'courses': courses}
  return render(request, 'checklist/course_list.html', context)

def program_list(request):
  programs = Program.objects.all()
  context = {'programs': programs}
  return render(request, 'checklist/program_list.html', context)

def program_search(request):
  programcourses = ProgramCourses.objects.select_related('programs', 'courses').all()
  order_by = request.GET.get('order_by', 'programs__level_abbrev')
  programcourses_list = programcourses.order_by(order_by)

  context = {'programcourses_list': programcourses_list}
  return render(request, 'checklist/program_search.html', context)

  """ 
  1. gets related models for each programcourse
  2. uses parameter for order_by or default level_abbrev
  3. can take in parameter for order_by
  4. returns sorted data
  """


def add_course(request):
  submitted = False
  """if is_create:              need to fix this, else will add duplicates
    instance = None
  else:
    instance = get_object_or_404(Course, pk=pk)"""
  if request.method == "POST":
    form = CourseForm(request.POST, instance=instance)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/addcourse?submitted=True')
  else: 
    form = CourseForm
    if 'submitted' in request.GET:
      submitted = True
  return render(request, "checklist/add_course.html", {'form': form, 'submitted': submitted})  #'instance': instance,


def add_program(request):
  submitted = False
  if request.method == "POST":
    form = ProgramForm(request.POST)    #need to fix this, else will add duplicates
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/addprogram?submitted=True')
  else: 
    form = ProgramForm
    if 'submitted' in request.GET:
      submitted = True
  return render(request, "checklist/add_program.html", {'form': form, 'submitted': submitted})

def link_course_program(request):     #need to set this instead...?
  submitted = False
  if request.method == "POST":
    form = ProgramCoursesForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/linkcourseprogram?submitted=True')
  else: 
    form = ProgramCoursesForm
    if 'submitted' in request.GET:
      submitted = True
  return render(request, "checklist/link_course_program.html", {'form': form, 'submitted': submitted})


def upload_program(request):
  submitted = False
  if request.method == "POST":
    form = UploadForm(request.POST, request.FILES)
    if form.is_valid():
      save_path = settings.MEDIA_ROOT / form.cleaned_data["file_upload"].name
      with open(save_path, "wb") as output_file:
        for chunk in form.cleaned_data["file_upload"].chunks():
          output_file.write(chunk)
    return HttpResponseRedirect('/uploadprogram?submitted=True')
  else:
    form = UploadForm()
    if 'submitted' in request.GET:
      submitted = True
  return render(request, "checklist/upload_program.html", {"form": form, 'submitted': submitted})


"""  did not work
class ProgramUploadView(View):
  def get(self, request):
    template_name = 'upload_program.html'
    return render(request, template_name)
  def post(self, request):
    coursefile = io.TextIOWrapper(request.FILES['coursefile'].file)
    coursedict = csv.DictReader(coursefile)
    courselist = list(coursedict)
    courseobjs = [
        Course(
          subj_abbrev=row['subj_abbrev'],
          no=row['no'],
          name=row['name'],
          hours=row['hours'],
          programs=program,     #fk value
        )
        for row in courselist
    ]
    try:
      message = Course.objects.bulk_create(courseobjs)
      returnmessage = {"status_code": 200}
      print('courses added')
    except Exception as e:
      print('Error importing:', e)
      returnmessage = {"status_code": 500}

    return JsonResponse(returnmessage)

"""