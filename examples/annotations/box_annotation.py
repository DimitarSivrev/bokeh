''' A timeseries plot of glucose data readings. This example demonstrates
adding box annotations as well as a multi-line title.

.. bokeh-example-metadata::
    :sampledata: glucose
    :apis: bokeh.plotting.figure.line, bokeh.plotting.figure.scatter, bokeh.models.annotations.BoxAnnotation
    :refs: :ref:`userguide_annotations` > :ref:`userguide_annotations_box_annotations`
    :keywords: box annotation, time series

'''
from bokeh.models import BoxAnnotation
from bokeh.plotting import figure, output_file, show
from bokeh.sampledata.glucose import data

output_file("box_annotation.html", title="box_annotation.py example")

TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

#reduce data size
data = data.loc['2010-10-06':'2010-10-13']

p = figure(x_axis_type="datetime", tools=TOOLS)

p.line(data.index.to_series(), data['glucose'], line_color="gray", line_width=1, legend_label="glucose")

low_box = BoxAnnotation(top=80, fill_alpha=0.2, fill_color='#D55E00')
mid_box = BoxAnnotation(bottom=80, top=180, fill_alpha=0.2, fill_color='#0072B2')
high_box = BoxAnnotation(bottom=180, fill_alpha=0.2, fill_color='#D55E00')

p.add_layout(low_box)
p.add_layout(mid_box)
p.add_layout(high_box)

p.title.text = "Glucose Range"
p.xgrid[0].grid_line_color=None
p.ygrid[0].grid_line_alpha=0.5
p.xaxis.axis_label = 'Time'
p.yaxis.axis_label = 'Value'

show(p)
