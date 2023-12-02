from plotly.offline import plot
import plotly.graph_objs as graphs
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import datetime
from django.db.models import Count
from checklist.models import Course, Program, ProgramCourses

def gen_bar(x_axis, y_axis):
  pcount= Program.objects.all().count()
  ccount = Course.objects.all().count()
  x = ['program', 'course']
  y = [pcount, ccount]
  barchart = px.bar(x=x, y=y)
  barchart.update_layout(title_text = "New courses added this year")
  barchart1 = barchart.to_html()
  


  #pc.values('programs').annotate(coursecount=Count('courses', distinct=True))  would need to look at level + major + specialization, not sure how to do this
  figure = graphs.Figure()
  bar = graphs.Bar(x=x_axis, y=y_axis)
  # program = Program.objects.all()
  # prog_totcourse = Program.objects.annotate(total_courses=Count('programcourses__courses'))
  # bar = px.bar(x=program, y=prog_totcourse)
  # fig = 

# def gen_scatterplot(x_axis, y_axis):
#   figure = graphs.Figure()
#   scatter = graphs.Scatter(x=x_axis, y=y_axis)
#   figure.add_trace(scatter)
#   return plot(figure, output_type='div')


# def gen_html(plot_html):
#   html_content = "<html><head><title>Plot</title></head><body>{}</body></html>".format(plot_html)
#   try:
#     with open('media/graphs/plot.html', 'w', encoding="utf-8") as plot_file:
#       plot_file.write(html_content)
#   except (IOError, OSError) as file_io_error:
#     print("Unable to generate plot file.Exception: {}".format(file_io_error))

# if __name__ == '__main__':
#     x = [1,2,3,4,5]
#     y = [3,8,7,9,2]
#     plot_html = gen_scatterplot(x, y)
#     gen_html(plot_html)


# what might interesting to see?
# students intersted in courses over time (dont' have that info but could make it up)
# total number of is_core, is_major, is_degree for each program

