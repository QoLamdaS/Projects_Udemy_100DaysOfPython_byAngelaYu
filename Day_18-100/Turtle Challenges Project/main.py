import turtle
import random

turtle.colormode(255) #! Tell turtle to accept RGB values from 0–255
def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

t = turtle.Turtle()
the_screen = turtle.Screen()
t.shape("turtle")
t.pensize(1)
t.speed(0)

for i in range(200):
    t.color(random_colors())
    t.circle(100)
    t.setheading(int(i * 4 * 360 / 200))


the_screen.mainloop()