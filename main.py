from turtle import Turtle, Screen

square_turtle = Turtle()
square_turtle.shape("turtle")
square_turtle.color("blue")

i = 3
times = 1
degrees = 360

while times <= 9:
    for _ in range(i):
        if i == 3:
            square_turtle.forward(100)
            square_turtle.right(degrees/i)
            square_turtle.color("black")
        elif i == 4:
            square_turtle.forward(100)
            square_turtle.right(degrees/i)
            square_turtle.color("blue")
        elif i == 5:
            square_turtle.forward(100)
            square_turtle.right(degrees/i)
            square_turtle.color("brown")
        elif i == 6:
            square_turtle.forward(100)
            square_turtle.right(degrees/i)
            square_turtle.color("magenta")
        elif i == 7:
            square_turtle.forward(100)
            square_turtle.right(degrees/i)
            square_turtle.color("orange")
        elif i == 8:
            square_turtle.forward(100)
            square_turtle.right(degrees/i)
            square_turtle.color("green")
        elif i == 9:
            square_turtle.forward(100)
            square_turtle.right(degrees/i)
            square_turtle.color("purple")
        elif i == 10:
            square_turtle.forward(100)
            square_turtle.right(degrees/i)
            square_turtle.color("red")
    i += 1
    times += 1

screen = Screen()
screen.exitonclick()