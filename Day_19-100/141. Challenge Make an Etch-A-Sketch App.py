import turtle

t = turtle.Turtle()
screen = turtle.Screen()
t.speed(0)
def move_forward():
    t.forward(20)
def move_backward():
    t.backward(20)
def turn_left():
    t.left(20)
def turn_right():
    t.right(20)
def clear_drawing():
    t.clear()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_drawing, "c")

screen.mainloop()