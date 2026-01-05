import turtle
import random

turtle.colormode(255) #! Tell turtle to accept RGB values from 0–255
def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

directions = [0, 90, 180, 270]
a_turtle = turtle.Turtle()
the_screen = turtle.Screen()
a_turtle.shape("turtle")
a_turtle.pensize(25)
a_turtle.speed(0)

for _ in range(200):
    a_turtle.color(random_colors()) # NOW WORKS!!!!!!!
    a_turtle.setheading(random.choice(directions))
    a_turtle.forward(30)


the_screen.mainloop()