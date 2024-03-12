from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.models import ColumnDataSource
import random

# Set up the output
output_notebook()

# Create a figure
p = figure(title="Spot Painting", x_range=(0, 100), y_range=(0, 100), tools="")

# Create a data source
source = ColumnDataSource(data=dict(x=[], y=[]))

# Create a scatter plot
p.circle('x', 'y', source=source, size=10, color="black")

# Add data to the source
for i in range(1000):
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    source.stream(dict(x=[x], y=[y]))

# Show the plot
show(p)