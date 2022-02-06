import turtle
import random


ted = turtle.Turtle()
turtle.colormode(255)
ted.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_random = (r, g, b)
    return color_random


counter = 1

for i in range(100):
    ted.circle(counter)
    ted.setheading(ted.heading() + counter)
    counter += 1

screen = turtle.Screen()
screen.exitonclick()
