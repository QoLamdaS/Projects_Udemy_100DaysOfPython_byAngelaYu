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
t = turtle.Turtle()
the_screen = turtle.Screen()
t.shape("turtle")
t.pensize(25)
t.speed(0)

for _ in range(200):
    t.color(random_colors()) # NOW WORKS!!!!!!!
    t.setheading(random.choice(directions))
    t.forward(30)


the_screen.mainloop()