from turtle import Turtle, Screen
from the_snake_body import SnakeBody
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("the Snake Game VERSION!!!!!!")
screen.tracer(0)

snake = SnakeBody()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.mainloop()
