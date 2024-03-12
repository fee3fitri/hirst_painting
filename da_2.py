import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Set up the colors
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Function to create a spot
def create_spot(x, y, color, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(size)
    t.end_fill()

# Create the spots
for i in range(1000):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    color = random.choice(colors)
    size = random.randint(5, 20)
    create_spot(x, y, color, size)

# Keep the window open
turtle.done()