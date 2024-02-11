import colorgram
from turtle import Turtle, Screen
import random


def random_color():
    num_color = 30
    colors = colorgram.extract('spot_painting.jpg', num_color)
    rgb_float = random.choice(colors).rgb
    return rgb_float


t = Turtle()
s = Screen()
s.colormode(255)

print(random_color())

t.pencolor(random_color())
t.dot(20)
t.penup()
t.forward(50)



s.exitonclick()