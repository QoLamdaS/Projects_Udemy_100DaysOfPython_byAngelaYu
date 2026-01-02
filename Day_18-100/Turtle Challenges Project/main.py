from turtle import Turtle
from turtle import Screen

a_turtle = Turtle()
a_turtle.shape("turtle")
a_turtle.color("red4")
for _ in range(4):
    a_turtle.forward(100)
    a_turtle.right(90)

the_screen = Screen()
the_screen.exitonclick()
