''' A stacked bar chart grouped into four groups using data in plain Python lists.

.. bokeh-example-metadata::
    :apis: bokeh.models.ColumnDataSource, bokeh.models.FactorRange, bokeh.plotting.figure.vbar_stack
    :refs: :ref:`userguide_bars` > :ref:`userguide_bars` > :ref:`userguide_bars_stacked_and_grouped`
    :keywords: bars, categorical, stacked, grouped

'''
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.plotting import figure

output_file("bar_stacked_grouped.html")

factors = [
    ("Q1", "jan"), ("Q1", "feb"), ("Q1", "mar"),
    ("Q2", "apr"), ("Q2", "may"), ("Q2", "jun"),
    ("Q3", "jul"), ("Q3", "aug"), ("Q3", "sep"),
    ("Q4", "oct"), ("Q4", "nov"), ("Q4", "dec"),

]

regions = ['east', 'west']

source = ColumnDataSource(data=dict(
    x=factors,
    east=[ 5, 5, 6, 5, 5, 4, 5, 6, 7, 8, 6, 9 ],
    west=[ 5, 7, 9, 4, 5, 4, 7, 7, 7, 6, 6, 7 ],
))

p = figure(x_range=FactorRange(*factors), height=250,
           toolbar_location=None, tools="")

p.vbar_stack(regions, x='x', width=0.9, alpha=0.5, color=["blue", "red"], source=source,
             legend_label=regions)

p.y_range.start = 0
p.y_range.end = 18
p.x_range.range_padding = 0.1
p.xaxis.major_label_orientation = 1
p.xgrid.grid_line_color = None
p.legend.location = "top_center"
p.legend.orientation = "horizontal"

show(p)
