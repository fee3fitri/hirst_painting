from bokeh.plotting import figure, show
from bokeh.io import output_notebook
import random

# Set up the output
output_notebook()

# Create a figure
p = figure(title = "Spot Painting", x_range = (-300, 300), y_range = (-300, 300), tools = "")

# Create a list of random x and y coordinates, colors and sizes for the spots
x = [random.randint(-300, 300) for _ in range(1000)]
y = [random.randint(-300, 300) for _ in range(1000)]
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
sizes = [random.randint(1, 5) for _ in range(1000)]

# Create the spots
p.circle(x, y, size = sizes, color = colors, alpha = 0.6)

# Show the plot
show(p)