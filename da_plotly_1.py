import plotly.graph_objects as go
import random

# Create a list of random x and y coordinates, colors and sizes for the spots
x = [random.randint(-300, 300) for _ in range(1000)]
y = [random.randint(-300, 300) for _ in range(1000)]
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
sizes = [random.randint(1, 5) for _ in range(1000)]

# Create the scatter plot
fig = go.Figure(data=go.Scatter(
    x=x,
    y=y,
    mode='markers',
    marker=dict(
        size=sizes,
        color=colors,
        opacity=0.6
    )
))

# Show the plot
fig.show()