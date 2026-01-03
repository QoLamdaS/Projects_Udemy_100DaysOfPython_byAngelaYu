import turtle
import random

a_turtle = turtle.Turtle()
the_screen = turtle.Screen()
a_turtle.shape("turtle")

def draw_dash_line(dash_length, space_length, total_dashes):
    """
    * Draws a dashed line.
    ! param is a function Parameters

    ->param dash_length: The length of each drawn segment.
    ->param space_length: The length of each empty space.
    ->param total_dashes: The total number of dashes to draw.
    """
    for _ in range(total_dashes):
        a_turtle.pendown()       # Start drawing
        a_turtle.forward(dash_length)
        a_turtle.penup()         # Stop drawing
        a_turtle.forward(space_length)
def custom_shape(sides):
    angle = 360 / sides
    a_turtle.color(random.choice(["red", "blue", "green", "yellow", "purple", "orange"]))
    for _ in range(sides):
        a_turtle.forward(100)
        a_turtle.right(angle)

for i in range(3, 11):
    custom_shape(i)





# draw_dash_line(10, 10, 15)

the_screen.mainloop()