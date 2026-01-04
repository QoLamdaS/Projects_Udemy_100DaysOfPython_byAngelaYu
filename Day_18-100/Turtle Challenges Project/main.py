import turtle
import random

directions = [0, 90, 180, 270]
colors = ["red", "blue", "green", "yellow", "purple", "orange"]
a_turtle = turtle.Turtle()
the_screen = turtle.Screen()
a_turtle.shape("turtle")
a_turtle.pensize(25)
a_turtle.speed(0)
for _ in range(200):
    a_turtle.color(random.choice(colors))
    a_turtle.setheading(random.choice(directions))
    a_turtle.forward(30)


the_screen.mainloop()