import time

# from weasyprint import HTML, CSS
# from .models import Program, Course, ProgramCourses
from django.http import HttpResponse

# from django.template.loader import render_to_string
# from django.utils.text import slugify


# def generate_pdf(url, pdf_file):
#   print("Generating PDF...")
#   HTML(url).write_pdf(pdf_file, stylesheets=[CSS(string='body { font-size: 12px }')])
#   if __name__ == '__main__':
#     url = 'http://text.npr.org'
#     pdf_file = 'media/pdfs/course.pdf'
#     generate_pdf(url, pdf_file)


# https://docs.djangoproject.com/en/4.2/howto/outputting-pdf/
# https://doc.courtbouillon.org/weasyprint/stable/
# https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#quickstart


# def checklist_pdf(request, checklist_id):
#   programcourses = ProgramCourses.objects.select_related('programs', 'courses').all()
#   checklist = get_object_or_404(ProgramCourses, pk=pk)
#   not sure...
#   response = HttpResponse(content="application/pdf")
#   response['Content-Disposition'] = "inline; filename={date}-checklist.pdf".format(date=checklist.created.strftime('%y-%m-%d'),name=slugify(checklist.programs.level_abbrev, checklist.programs.major_abbrev),)
#   html=render_to_string("checklist/checklist_pdf.html", {'checklist': checklist,})
#   HTML(string=html).write_pdf(response)
#   return response


#   1. create function to get checklist by id
#     show all related courses, is_core, is_major, is_degree -> already exists

#   2. create function to generate pdf for the info on this webpage...?


#   3. add print icon to this webpage
#       downloads pdf of checklist


#   4.  ??link function to generate pdf to print icon  ??


# Also do this with csv_output mmmmm....?
