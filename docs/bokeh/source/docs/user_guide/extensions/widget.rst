.. _userguide_extensions_examples_widget:

Adding a custom widget
----------------------

This example shows how to add a double-ended slider widget to the plot.

The single normal Bokeh slider controls the power of the line.
The double ended sliders control the x range for the line.

.. bokeh-plot:: __REPO__/examples/extensions/widget.py
    :source-position: none

.. can't use __REPO__ with literalinclude, unfortunately

Python script:

.. literalinclude:: ../../../../../../examples/extensions/widget.py
   :language: python

TypeScript for IonRangeSlider:

.. literalinclude:: ../../../../../../examples/extensions/ion_range_slider.ts
   :language: typescript
