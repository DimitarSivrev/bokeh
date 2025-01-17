'''  A grid plot that shows four figures that use different glyphs.

.. bokeh-example-metadata::
    :apis: bokeh.layouts.gridplot
    :refs: :ref:`userguide_layout` > :ref:`userguide_layout_gridplot`
    :keywords: grid, gridplot

'''
from bokeh.io import output_file, show
from bokeh.layouts import gridplot
from bokeh.plotting import figure

output_file("layout_grid.html")

x = list(range(11))
y0 = x
y1 = [10 - i for i in x]
y2 = [abs(i - 5) for i in x]

# create three plots
s1 = figure(background_fill_color="#fafafa")
s1.circle(x, y0, size=12, alpha=0.8, color="#53777a")

s2 = figure(background_fill_color="#fafafa")
s2.triangle(x, y1, size=12, alpha=0.8, color="#c02942")

s3 = figure(background_fill_color="#fafafa")
s3.square(x, y2, size=12, alpha=0.8, color="#d95b43")

# make a grid
grid = gridplot([[s1, s2], [None, s3]], width=250, height=250)

show(grid)
