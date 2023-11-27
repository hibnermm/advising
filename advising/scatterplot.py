from plotly.offline import plot
import plotly.graph_objs as graphs


def gen_scatterplot(x_axis, y_axis):
  figure = graphs.Figure()
  scatter = graphs.Scatter(x=x_axis, y=y_axis)
  figure.add_trace(scatter)
  return plot(figure, output_type='div')


def gen_html(plot_html):
  html_content = "<html><head><title>Plot</title></head><body>{}</body></html>".format(plot_html)
  try:
    with open('media/graphs/plot.html', 'w', encoding="utf-8") as plot_file:
      plot_file.write(html_content)
  except (IOError, OSError) as file_io_error:
    print("Unable to generate plot file.Exception: {}".format(file_io_error))

if __name__ == '__main__':
    x = [1,2,3,4,5]
    y = [3,8,7,9,2]
    plot_html = gen_scatterplot(x, y)
    gen_html(plot_html)