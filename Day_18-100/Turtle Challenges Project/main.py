from turtle import Turtle
from turtle import Screen

a_turtle = Turtle()
a_turtle.shape("turtle")
a_turtle.color("red4")
# for _ in range(4):
#     a_turtle.forward(100)
#     a_turtle.right(90)

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

draw_dash_line(10, 10, 15)

the_screen = Screen()
the_screen.exitonclick()
